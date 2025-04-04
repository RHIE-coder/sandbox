import streamlit as st
import ollama
import json
from pathlib import Path
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from rich.console import Console
console = Console()

st.set_page_config(page_title="XPath 추출기", layout="wide")
st.title("🔍 XPath 자동 추출기")

# --- 입력 영역 ---
url = st.text_input("🌐 웹페이지 URL", "https://stg-new-client.airspeechedu.io/login")
ui_spec_input = st.text_area("🧾 UI 요소 목록 (한 줄씩 입력)", """
로그인 버튼
아이디 입력필드
비밀번호 입력필드
비밀번호 재설정 링크
회원가입 링크
""")

# 상태 저장용 변수
if 'xpath_result' not in st.session_state:
    st.session_state.xpath_result = None
if 'html_content' not in st.session_state:
    st.session_state.html_content = None

# --- 함수 정의 ---
def get_page_html(url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        content = page.content()
        return content, page

def extract_main_or_form(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    main = soup.find('main')
    if main:
        return str(main)
    form = soup.find('form')
    if form:
        return str(form)
    return html[:8000]  # fallback

def get_xpath_from_llm(html: str, ui_schema: list):
    console.print(html)
    prompt = "다음은 웹페이지의 HTML 일부입니다.\n"
    prompt += "당신의 임무는 HTML의 구조를 기반으로 아래에 명시된 UI 요소들의 정확한 XPath 경로를 추론하는 것입니다.\n\n"
    prompt += "⚠️ XPath 경로는 반드시 **HTML의 계층 구조만을 기반**으로 생성해야 하며, 다음 조건을 반드시 지켜야 합니다:\n"
    prompt += "- XPath는 `/html/body/...`와 같은 절대 경로 형식으로 작성해야 합니다.\n"
    prompt += "- `@name`, `@type`, `@class`, `@placeholder` 등 **속성을 기반으로 추론하거나 필터링하지 마세요**.\n"
    prompt += "- `text()`, `contains()`, `normalize-space()` 등 텍스트 기반 접근도 금지합니다.\n"
    prompt += "- 모든 XPath는 계층적인 위치 기반으로 작성되어야 하며, 각 요소의 정확한 태그 순서를 반영해야 합니다.\n"
    prompt += "- 중복을 피하고, 문맥이 모호한 경우에도 **텍스트, 클래스, 이름에 의존하지 말고 태그 계층만으로 판단**하세요.\n"
    prompt += "- 예를 들어 `//a[text()='회원가입']` → ❌ 사용 금지, 반드시 `/html/body/.../a` 형식으로 추출해야 합니다.\n"
    prompt += "- 출력은 JSON 형식으로, 설명 없이 결과만 출력하세요.\n\n"
    prompt += """
절대 XPath 경로는 실제 DOM 구조에 존재해야 하며, DOM의 `<form>` → `<div>` 구조를 분석해서 실제 존재하는 위치 기반으로 작성해야 합니다.
- 추측하지 말고 구조만 기반으로 판단하세요.
- XPath를 직접 DOM 트리를 탐색하듯이 중첩 구조 그대로 생성하세요.
"""

    prompt += "HTML 요약:\n"
    prompt += html + "...\n\n"

    prompt += "UI 요소 목록:\n"
    for label in ui_schema:
        prompt += f"- {label}\n"

    prompt += """
    예시 출력:
    ```json
    {
    "회원가입 링크": "/html/body/main/div/div[2]/form/div/div[2]/div/div/a/p",
    "로그인 버튼": "/html/body/main/div/div[2]/form/div/div[2]/button"
    }
    """

    prompt += "\n출력은 위 형식과 정확히 동일하게 JSON만 반환하세요."






    response = ollama.chat(
        model="gemma3:4b",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"].strip()

def validate_xpath_mapping(html, mapping):
    results = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html)
        for label, xpath in mapping.items():
            print(label, xpath)
            try:
                found = page.locator(f"xpath={xpath}").count()
                results[label] = f"✅ {found} element(s) found" if found > 0 else "❌ Not found"
            except Exception as e:
                results[label] = f"❌ Error: {e}"
        browser.close()
    return results

# --- XPath 추출 실행 ---
if st.button("🚀 XPath 추출하기"):
    with st.spinner("HTML 가져오는 중..."):
        html, _ = get_page_html(url)
        st.session_state.html_content = html

    ui_spec = [line.strip() for line in ui_spec_input.strip().split("\n") if line.strip()]
    short_html = extract_main_or_form(html)

    with st.spinner("LLM에게 요청 중..."):
        result = get_xpath_from_llm(short_html, ui_spec)

    st.session_state.xpath_result = result
    st.subheader("🧾 결과:")
    st.code(result, language="json")
import re
import json

def extract_json_from_block(text: str) -> dict:
    """
    LLM 응답 중 ```json ... ``` 으로 감싸진 JSON을 추출하여 파싱
    """
    # 정규 표현식으로 ```json ... ``` 블록만 추출
    match = re.search(r"```json\s*({.*?})\s*```", text, re.DOTALL)
    if match:
        json_str = match.group(1)
    else:
        # fallback: 그냥 중괄호로 된 블록만 추출
        match = re.search(r"(\\{.*\\})", text, re.DOTALL)
        if match:
            json_str = match.group(1)
        else:
            raise ValueError("JSON 형식이 감지되지 않았습니다.")

    return json.loads(json_str)

def retry_failed_items(html: str, original_map: dict, result_check: dict):
    failed_labels = [label for label, status in result_check.items() if status.startswith("❌")]
    if not failed_labels:
        return {}
    return get_xpath_from_llm(html, failed_labels)

# --- XPath 검증 버튼 ---
if st.session_state.xpath_result and st.session_state.html_content:
    if st.button("✅ XPath 결과 검증하기"):
        try:
            xpath_map = extract_json_from_block(st.session_state.xpath_result)
            with st.spinner("XPath를 검증 중입니다..."):
                result_check = validate_xpath_mapping(st.session_state.html_content, xpath_map)
            st.subheader("🔎 검증 결과:")
            for label, status in result_check.items():
                st.write(f"- {label}: {status}")

            # 실패한 항목 재시도
            if any(v.startswith("❌") for v in result_check.values()):
                if st.button("♻️ 실패 항목 재요청하기"):
                    with st.spinner("실패 항목 재요청 중..."):
                        short_html = extract_main_or_form(st.session_state.html_content)
                        retry_result = retry_failed_items(short_html, xpath_map, result_check)
                        st.code(retry_result, language="json")

        except Exception as e:
            st.error(f"검증 중 오류 발생: {e}")