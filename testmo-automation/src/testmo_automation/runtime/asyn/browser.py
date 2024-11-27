from playwright.async_api import async_playwright, Playwright

async def start_playwright():
    return await async_playwright().start()

async def get_chromium(playwright:Playwright, options:dict=None):
    if options is None:
        options = dict(
            headless=False,
            # headless=True,
            slow_mo=500,
            # args=[
            #     "--start-maximized",
            # ],
        )
    chromium = playwright.chromium
    return await chromium.launch(**options)


async def load_default_page(*, reset_session=False):
    playwright = await start_playwright()
    chrome = await get_chromium(playwright)
    context = None
    try:
        if reset_session:
            context = await chrome.new_context()
        else:
            context = await chrome.new_context(storage_state=".auth/state.json")
    except:
        context = await chrome.new_context()
    page = await context.new_page()
    await page.set_viewport_size({"width": 950, "height": 1800})
    page.set_default_timeout(6000)
    return page