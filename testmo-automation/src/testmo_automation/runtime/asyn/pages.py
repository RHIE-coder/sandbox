from testmo_automation.config import load_ini_config, TestmoUrlBuilder
from abc import ABC, abstractmethod
import os

##########################################
#
#          TestmoPage
#
##########################################
class TestmoPage(ABC):
    def __init__(self, page):
        self.__page = page
        self.components()
        wp = load_ini_config()["project"]["workspace"]
        self.url_builder = TestmoUrlBuilder(wp)
    
    @property
    def page(self):
        return self.__page

    async def goto(self):
        await self.__page.goto(self.url())


    async def wait_for_no_overlay(self):
        overlay = self.page.locator('.blockUI.blockOverlay')
        await overlay.wait_for(state="detached", timeout=5000)
    
    @abstractmethod
    def url(self):
        raise ReferenceError("the url is empty")

    @abstractmethod
    def components(self):
        raise ReferenceError("should override components()")

##########################################
#
#          Login
#
##########################################
class Login(TestmoPage):
    
    def url(self):
        return self.url_builder.home() + "/auth/login"

    def components(self):
        self.input_email = self.page.locator(selector="input[name='email']")
        self.input_pawssword = self.page.locator(selector="input[name='password']")
        self.btn_login = self.page.locator(selector="button[type='submit']")

    async def login(self):
        await self.input_email.type(load_ini_config()["account"]["username"])
        await self.input_pawssword.type(load_ini_config()["account"]["password"])
        await self.btn_login.click()
        await self.page.wait_for_url(f"{self.url_builder.home()}/", timeout=3000)
        
        if not os.path.exists(".auth"):
            os.makedirs(".auth")

        await self.page.context.storage_state(path=".auth/state.json")

##########################################
#
#          Repository
#
##########################################
class Repository(TestmoPage):

    def url(self):
        repo_num = load_ini_config()["project"]["repository_num"]
        return self.url_builder.repo(repo_num).build_url()

    def components(self):
        self.groups = self.page.locator(selector="div[data-name='groups']")
        self.not_expanded_list = self.groups.locator("[data-name]").locator('[class*="tree__node--expandable"]:not([class*="tree__node--expanded"])')
        self.clickable_to_expand = self.not_expanded_list.first.locator(".tree__node__entry__expansion__expand")

    async def not_expanded_folder_count(self):
        return await self.not_expanded_list.count()

    async def collapse_all_folders(self):
        retries = 3

        while await self.not_expanded_folder_count() != 0:
            try:
                # Wait for the overlay to disappear before clicking
                await self.wait_for_no_overlay()
                await self.clickable_to_expand.first.click()
        
            except Exception as e:
                print("error")
                print(e)
                retries-=1
            finally:
                if retries == 0:
                    raise RuntimeError("retry over")
    
    async def group_info(self):
        print("asdfasdfadsfas")