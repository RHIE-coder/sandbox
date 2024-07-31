from playwright.sync_api import Page

class Login:

    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.get_by_placeholder('Email')
        self.password_input = page.get_by_placeholder('Password')
        self.signin_button = page.get_by_role('button', name='Sign in')

    def goto(self):
        self.page.goto('/#/login')
