import pytest
from playwright.sync_api import Page, expect
import logging

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    print("before the test runs")

    # Go to the starting url before each test.
    timeout = 5000
    page.set_default_navigation_timeout(timeout)
    page.set_default_timeout(timeout)
    page.goto("https://demo.playwright.dev/todomvc")
    yield
    
    print("after the test runs")

# test_[detail category]_[TC No.]
def test_detail_1(page: Page):
    """
    todos 타이틀이 노출되어야 한다
    """
    expect(page.get_by_role("heading", name="todos")).to_be_visible()


def test_detail_2(page: Page):
    """
    입력창에 "What needs to be done?" placeholder 문구가 노출되어야 한다
    """
    expect(page.get_by_placeholder("What needs to be done?")).to_be_visible()

def test_detail_3(page: Page):
    """
    영문 대소문자, 한글, 숫자, 특수문자, 공백이 입력되어야 한다
    """
    page.get_by_placeholder("What needs to be done?").fill("Rhie1234 민!@#")

def test_detail_4(page: Page):
    """
    입력한 문구가 입력창 길이를 넘어가면 wrap되어야 한다.
    """
    logging.warning("manual testing")
    pass

def test_detail_5(page: Page):
    """
    precondition: test_detail_3
    엔터키를 누르면 입력한 문구로 todo 아이템이 생성되어야 이다
    """
    page.get_by_placeholder("What needs to be done?").fill("Rhie1234 민!@#")
    page.get_by_placeholder("What needs to be done?").press("Enter")

def test_detail_6(page: Page):
    """
    precondition: test_detail_5
    todo 아이템의 토글을 누르면 체크되어야 한다
    """
    page.get_by_placeholder("What needs to be done?").fill("Rhie1234 민!@#")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_label("Toggle Todo").click()


def test_detail_7(page: Page):
    """
    precondition: test_detail_5
    todo 아이템의 'X' 표시를 누르면 todo 아이템이 사라져야 한다
    """
    page.get_by_placeholder("What needs to be done?").fill("Rhie1234 민!@#")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_test_id("todo-title").hover()
    page.get_by_label("Delete").click()
