from rich.console import Console
console = Console()

import base64

def image_to_base64(path: str) -> str:
    with open(path, 'rb') as f:
        encoded = base64.b64encode(f.read()).decode('utf-8')
    return encoded

from playwright.sync_api import sync_playwright

def get_page_html(url: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        content = page.content()
        browser.close()
        return content


import ollama

def get_xpath_from_llm(html: str, ui_schema: dict, image_base64: str = None):
    prompt = "다음은 웹페이지의 HTML과 스크린샷입니다.\n"
    prompt += "HTML과 스크린샷을 분석해서 [UI 요소 설명]에 맞는 XPath를 맵핑하여 보여주세요\n\n"
    prompt += f"[HTML]\n{html}...\n\n"  # 모델에 따라 길이 제한 필요

    prompt += "\n[UI 요소 설명 목록]\n"
    for label in ui_schema:
        prompt += f"- {label}\n"

    if image_base64:
        prompt += "\n[스크린샷: base64 이미지 포함]"
    
    console.log(prompt)

    response = ollama.chat(
        model="gemma3:4b",
        messages=[
            {"role": "user", "content": prompt, "images": [image_base64] if image_base64 else []}
        ]
    )

    return response["message"]["content"]

ui_spec = [
    "로그인 버튼",
    "아이디 입력필드",
    "비밀번호 입력필드",
    "비밀번호 재설정 링크",
]

from pathlib import Path

html = get_page_html("https://stg-new-client.airspeechedu.io/login")
image_b64 = image_to_base64(str(Path().resolve() / "assets" / "로그인.png"))
xpath_mapping = get_xpath_from_llm(html, ui_spec, image_b64)

print(xpath_mapping)
