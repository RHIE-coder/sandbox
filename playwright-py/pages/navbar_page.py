from playwright.sync_api import Page

class Navbar:

    def __init__(self, page: Page):
        self.page = page

    def user_link(self, username: str):
        return self.page.get_by_role('link', name=username)
