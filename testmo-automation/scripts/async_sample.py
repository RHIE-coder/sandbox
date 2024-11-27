import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # GUI 모드로 실행
        page = await browser.new_page()
        await page.goto("https://example.com")

        print("브라우저가 멈춘 상태로 유지됩니다. 종료하려면 Ctrl+C를 누르세요.")
        await asyncio.Event().wait()  # 무기한 대기

asyncio.run(main())