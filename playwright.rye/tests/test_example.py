import re
import pytest
from playwright.sync_api import BrowserContext, Page, expect

@pytest.fixture(scope="session")
def browser_context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(browser_context: BrowserContext):
    page = browser_context.new_page()
    page.goto("https://playwright.dev/")
    yield page
    page.close()

class TestClass:
    def test_has_title(self, page: Page):
        expect(page).to_have_title(re.compile("Playwright"))

    def test_get_started_link(self, page: Page):
        page.get_by_role("link", name="Get started").click()
        expect(page.get_by_role("heading", name="Installation")).to_be_visible()
