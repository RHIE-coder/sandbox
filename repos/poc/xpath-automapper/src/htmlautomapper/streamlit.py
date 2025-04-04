import streamlit as st
import base64
import ollama
from pathlib import Path
from playwright.sync_api import sync_playwright

st.set_page_config(page_title="XPath 추출기", layout="wide")
st.title("🔍 XPath 자동 추출기")

# --- 입력 영역 ---
url = st.text_input("🌐 웹페이지 URL", "https://stg-new-client.airspeechedu.io/login")
ui_spec_input = st.text_area("🧾 UI 요소 목록 (한 줄씩 입력)", """
로그인 버튼
아이디 입력필드
비밀번호 입력필드
비밀번호 재설정 링크
""")

uploaded_image = st.file_uploader("🖼️ 스크린샷 업로드 (PNG, JPG)", type=["png", "jpg", "jpeg"])

# --- 함수 정의 ---
def image_to_base64(file) -> str:
    return base64.b64encode(file.read()).decode("utf-8")

def get_page_html(url: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        content = page.content()
        browser.close()
        return content

def get_xpath_from_llm(html: str, ui_schema: list, image_base64: str = None):
    prompt = "다음은 웹페이지의 HTML과 스크린샷입니다.\n"
    prompt += "HTML과 스크린샷을 분석해서 [UI 요소 설명]에 맞는 XPath를 맵핑하여 보여주세요\n\n"
    prompt += f"[HTML]\n{html[:8000]}...\n\n"  # 모델에 따라 길이 제한 필요

    prompt += "\n[UI 요소 설명 목록]\n"
    for label in ui_schema:
        prompt += f"- {label}\n"

    if image_base64:
        prompt += "\n[스크린샷: base64 이미지 포함]"

    response = ollama.chat(
        model="gemma3:4b",
        messages=[
            {"role": "user", "content": prompt, "images": [image_base64] if image_base64 else []}
        ]
    )

    return response["message"]["content"]

# --- 실행 ---
if st.button("🚀 XPath 추출하기"):
    with st.spinner("HTML 가져오는 중..."):
        html = get_page_html(url)

    ui_spec = [line.strip() for line in ui_spec_input.strip().split("\n") if line.strip()]
    image_b64 = image_to_base64(uploaded_image) if uploaded_image else None

    with st.spinner("LLM에게 요청 중..."):
        result = get_xpath_from_llm(html, ui_spec, image_b64)

    st.subheader("🧾 결과:")
    st.code(result, language="json")
