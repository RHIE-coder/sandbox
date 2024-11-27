import asyncio
from testmo_automation.runtime.asyn import browser
from testmo_automation.runtime.asyn.pages import Login
from testmo_automation.runtime.asyn import tools


async def main():
    page = await browser.load_default_page(reset_session=True)
    login: Login = Login(page)
    await login.goto()
    await login.login()
    await tools.wait_util_sigint()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("프로그램이 사용자에 의해 중지되었습니다.")