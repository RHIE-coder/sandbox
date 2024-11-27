import asyncio
from testmo_automation.runtime.asyn import browser
from testmo_automation.runtime.asyn.pages import Repository
from testmo_automation.runtime.asyn import tools


async def main():
    page = await browser.load_default_page()
    repo: Repository = Repository(page)
    await repo.goto()
    before_count = await repo.not_expanded_folder_count()
    if before_count > 0:
        await repo.collapse_all_folders()
    after_count = await repo.not_expanded_folder_count()
    if after_count > 0:
       raise RuntimeError("동작이 깔끔하게 마무리되지 못함") 
    await tools.wait_util_sigint()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("프로그램이 사용자에 의해 중지되었습니다.")