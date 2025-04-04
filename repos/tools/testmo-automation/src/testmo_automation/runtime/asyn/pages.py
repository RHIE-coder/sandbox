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

    async def goto(self, *args, **kwargs):
        await self.__page.goto(self.url(*args, **kwargs))


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

    def __init__(self, page):
        super().__init__(page)
        self.data_id_index_group = None
        self.data_ids = None

    def url(self):
        repo_num = load_ini_config()["project"]["repository_num"]
        return self.url_builder.repo(repo_num).build_url()

    def components(self):
        self.groups = self.page.locator(selector="div[data-name='groups']")
        self.not_expanded_list = self.groups.locator("[data-name]").locator('[class*="tree__node--expandable"]:not([class*="tree__node--expanded"])')
        self.clickable_to_expand = self.not_expanded_list.first.locator(".tree__node__entry__expansion__expand")
        self.datalist = self.groups.locator('[data-id]')
        self.top_datalist = self.groups.locator('> [data-id]')

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
    
    async def __folder_resolve(self, top_datalist, data_id_index_group):

        for idx in range(await top_datalist.count()):
            nth_target = top_datalist.nth(idx)
            
            data_id = await nth_target.get_attribute('data-id')
            data_name = await nth_target.get_attribute('data-name')

            data_id_index_group[data_id] = list()

            sub_targets = nth_target.locator('> .tree__node__subs').locator('> [data-id]')
            
            if await sub_targets.count() == 0:
                continue

            if await sub_targets.count() > 0:
                for iidx in range(await sub_targets.count()):
                    data_id_index_group[data_id].append(await sub_targets.nth(iidx).get_attribute('data-id'))
                await self.__folder_resolve(sub_targets, data_id_index_group)

    async def group_list(self, refresh=False):
        if not refresh:
            if self.data_ids is not None:
                return self.data_ids
            else:
                self.data_ids = list()
        for idx in range(await self.datalist.count()):
            target = self.datalist.nth(idx)
            data_id = await target.get_attribute('data-id')
            self.data_ids.append(data_id)
        return self.data_ids
            
    async def grouping(self, refresh=False):
        if not refresh:
            if self.data_id_index_group is not None:
                return self.data_id_index_group
            else:
                self.data_id_index_group = dict()
        await self.__folder_resolve(self.top_datalist, self.data_id_index_group)
        return self.data_id_index_group

##########################################
#
#          GroupCase
#
##########################################
class GroupCase(TestmoPage):

    def __init__(self, page):
        super().__init__(page)
        self.case_map = dict()
    
    def url(self, group_id, case_id=None):
        repo_num = load_ini_config()["project"]["repository_num"]
        if case_id is None:
            return self.url_builder.repo(repo_num).group(group_id).build_url()
        return self.url_builder.repo(repo_num).group(group_id).case(case_id).build_url()

    def components(self):
        self.elem_when_case_empty = self.page.get_by_text("Add test case")
        self.case_list = self.page.locator("tr[data-id]")
        self.btn_next = self.page.locator(selector="button[data-action='click->components--pagination#doNextPage']")
        self.btn_edit = self.page.get_by_text("Edit", exact=True)
        self.right_fields = self.page.locator('.dialog-split__right').locator(".field")
        self.left_side = self.page.locator('.dialog-split__left')
        self.left_upside = None
        self.left_downside = self.left_side.locator('[data-custom-field]')
        self.reference_field = self.left_downside.nth(12)
        
        self.template_field = self.right_fields.nth(0)
        self.state_field = self.right_fields.nth(1)
        self.estimate_field = self.right_fields.nth(2)
        self.issues_field = self.right_fields.nth(3) # 3, 4
        self.tags_field = self.right_fields.nth(5)
        self.test_level_field = self.right_fields.nth(6)
        self.sprint_field = self.right_fields.nth(7)
        self.sprint_field_input = self.sprint_field.locator('input')
        self.attachments_field = self.right_fields.nth(8)

        self.dropbox_popup = self.page.locator('.dropdown__popup__menu').locator('.dropdown__items')
        self.popup_dropitem = self.dropbox_popup.locator('[data-label]')
        
        self.editor_toolbar = self.reference_field.locator('[data-target="components--editor.toolbar"]')
        self.editor_toolbar_link = self.editor_toolbar.locator('[data-content="Link"]')
        self.editor_textarea = self.reference_field.locator('[data-target="components--editor.control"]')       

        
        self.btn_save = self.page.get_by_role("button", name="Save case")
                
    async def has_cases(self):
        return not (await self.elem_when_case_empty.is_visible())

    async def has_next_btn(self):
        return await self.btn_next.is_visible()

    async def has_next_page(self):
        return not await self.btn_next.is_disabled()
    
    async def case_mapping(self, group_id):
        
        try:
            await self.goto(group_id=group_id)
            await self.wait_for_no_overlay()

            self.case_map[group_id] = list()
    
            if not await self.has_cases():
                return len(self.case_map[group_id])
                
            for idx in range(await self.case_list.count()):
                target = self.case_list.nth(idx)
                self.case_map[group_id].append(await target.get_attribute('data-id'))
    
            if await self.has_next_btn() and await self.has_next_page():
                while await self.has_next_page():
                    await self.btn_next.click()
                    await self.wait_for_no_overlay()
                    for idx in range(await self.case_list.count()):
                        target = self.case_list.nth(idx)
                        await target.highlight()
                        self.case_map[group_id].append(await target.get_attribute('data-id'))
            return len(self.case_map[group_id])
        except Exception as e:
            print("[error occured]")
            print(f"group-id={group_id} / case-length={len(self.case_map[group_id])}")
            print(e)

    def get_cases(self):
        return self.case_map

    async def open_case_edit(self, gid, cid):
        await self.goto(gid, cid)
        await self.btn_edit.click()

    async def select_template(self, select):
        await self.template_field.click()
        for idx in range(await self.popup_dropitem.count()):
            target = self.popup_dropitem.nth(idx)
            item_name = await target.text_content()
            item_name = item_name.strip()
            if item_name == select:
                await target.click()

    async def select_tags(self, *tags):
        await self.tags_field.click()
        for tag_name in tags:
            target = self.popup_dropitem.get_by_text(tag_name)
            await target.click()

    async def fill_sprint(self, text):
        await self.sprint_field_input.fill(text)

    async def fill_reference(self, callback):
        await callback(self)

    async def save(self):
        await self.btn_save.click()