import re
from playwright.sync_api import Page, expect

# def test_signin_page(page: Page):
#     page.goto('http://localhost:3000/signin')
#     page.get_by_label("Username").click()
#     page.get_by_label("Username").fill("alice")
#     page.get_by_label("Password").click()
#     page.get_by_label("Password").fill("1234")
#     page.locator("[data-test=\"signin-submit\"]").click()

# def test_login_success(page: Page):
#     page.goto('/#/login')
#     page.get_by_placeholder('Email').type('test_playwright_login@test.com')
#     page.get_by_placeholder('Password').type('Test123456')
#     page.get_by_role('button', name='Sign in').click()
#     expect(page.get_by_role('link', name='test_playwright_login')).to_be_visible()
#     page.pause()


# from pages.login_page import Login
# from pages.navbar_page import Navbar

# def test_login_success(page: Page):
#     login = Login(page)
#     navbar = Navbar(page)
#     login.goto()
#     login.email_input.type('test_playwright_login@test.com')
#     login.password_input.type('Test123456')
#     login.signin_button.click()
#     expect(navbar.user_link('test_playwright_login')).to_be_visible()
#     page.pause()

# from playwright.sync_api import expect

def test_login_success(login, navbar):
    login.goto()
    login.email_input.type('test_playwright_login@test.com')
    login.password_input.type('Test123456')
    login.signin_button.click()
    expect(navbar.user_link('test_playwright_login')).to_be_visible()