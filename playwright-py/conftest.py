import pytest
from playwright.sync_api import Page
from pages.login_page import Login
from pages.navbar_page import Navbar


@pytest.fixture(scope='session')
def base_url():
    return 'https://react-redux.realworld.io/'


@pytest.fixture
def page(page: Page) -> Page:
    timeout = 10000
    page.set_default_navigation_timeout(timeout)
    page.set_default_timeout(timeout)
    return page


@pytest.fixture
def login(page) -> Login:
    return Login(page)

@pytest.fixture
def navbar(page) -> Navbar:
    return Navbar(page)