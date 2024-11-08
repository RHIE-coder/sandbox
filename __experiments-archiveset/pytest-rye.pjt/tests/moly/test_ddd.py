import pytest

# # 실패한 테스트를 추적하기 위한 전역 변수
failed_tests = set()

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 실패한 테스트를 기록
    print("&&& &&& &&& &&& &&&")
    if call.when == 'call' and call.excinfo is not None:
        failed_tests.add(item.name)

class TestEEE:

    # def test_eee1(self, common2):
    #     """ this is test sample """
    #     print(">> test_eee1()")
    #     print(common2)

    def test_eee2(self, common2):
        print(">> test_eee2()")
        print(common2)
        assert 1==2

    @pytest.mark.skipif(2==2, reason="Skipping because test_eee2 failed")
    def test_eee3(self, common2):
        print(">> test_eee3()")
        print(common2)
            
    # def test_eee4(self, common2):
    #     print(">> test_eee4()")
    #     print(common2)

    # def test_eee5(self, common2):
    #     print(">> test_eee5()")
    #     print(common2)
    
    def test_eee6(self, common2):
        print(">> test_eee6()")
        print(common2)
        # if fail here, go to test_eee2()
        assert 1 == 2

    def test_eee7(self, common2):
        print(">> test_eee7()")
        print(common2)

    # def test_eee8(self, common2):
    #     print(">> test_eee8()")
    #     print(common2)

    # def test_eee9(self, common2):
    #     print(">> test_eee9()")
    #     print(common2)