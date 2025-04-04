import pytest
from playwright.sync_api import sync_playwright


class 로그인:
    def __init__(self, page):
        self.page = page

    @property
    def 타이틀(self):
        return "로그인"

    @property
    def 아이디_입력_필드(self):
        return "아이디"
    
    @property
    def 비밀번호_입력_필드(self):
        return "비밀번호"
    
    @property
    def 로그인_버튼(self):
        return "로그인버튼"

@pytest.fixture(scope="class")
def 로그인화면(request, page):
    request.cls.page = 로그인(page)
    yield
    

@pytest.mark.usefixtures("로그인화면")
class Test로그인:
    def 로그인_페이지_타이틀_확인(self, 로그인화면:로그인):
        assert 로그인화면.타이틀 == "로그인"
    def 로그인_페이지_타이틀_확인1(self, 로그인화면:로그인):
        assert 로그인화면.타이틀 == "로그인"
    def 로그인_페이지_타이틀_확인2(self, 로그인화면:로그인):
        assert 로그인화면.타이틀 == "로그인"