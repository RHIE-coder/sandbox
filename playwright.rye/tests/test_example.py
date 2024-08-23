# import pytest
# import unittest

from playwright.sync_api import Page

# @pytest.fixture(scope="session")
# def setup(self, page: Page):
#     self.page = page
#     yield page
#     self.page.goto("https://www.google.com/")
# class MyTest(unittest.TestCase):

#     def test_foobar1(self, setup):
#         setup.locator("textarea[name='q']").fill("playwright1")
#         # self.page.locator("textarea[name='q']").fill("playwright1")

#     def test_foobar2(self):
#         self.page.locator("textarea[name='q']").fill("playwright2")

#     def test_foobar3(self):
#         self.page.locator("textarea[name='q']").fill("playwright3")

#     def test_foobar4(self):
#         self.page.locator("textarea[name='q']").fill("playwright4")

def step(page, description, func):
    print(f"Step: {description}")
    func(page)
    print(f"Completed: {description}")

def test_example(page):
    def step_1(page):
        page.goto("https://www.google.com/")
        
    def step_2(page):
        page.locator("textarea[name='q']").fill("playwright1")

    def step_3(page):
        page.locator("textarea[name='q']").fill("playwright2")

    def step_4(page):
        page.locator("textarea[name='q']").fill("playwright3")

    def step_5(page):
        page.locator("textarea[name='q']").fill("playwright4")

    step(page, "step 1", step_1)
    step(page, "step 2", step_2)
    step(page, "step 3", step_3)
    step(page, "step 4", step_4)
    step(page, "step 5", step_5)



# @pytest.fixture(scope="class")
# def fix_cls():
#     print('fix_cls')
#     data = []
#     assert len(data) == 0
#     yield data
#     assert len(data) == 3


# @pytest.fixture(scope="function")
# def fix_func(fix_cls):
#     print('fix_func')
#     # reset the data, reload the page
#     yield fix_cls
#     print('------>', fix_cls)


# class TestCls:
#     def test_a1(self, fix_func):
#         fix_func.append(1)

#     def test_a2(self, fix_func):
#         fix_func.append(2)

#     def test_a3(self, fix_func):
#         fix_func.append(3)