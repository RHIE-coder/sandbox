import pytest

# @pytest.fixture(autouse=True)
# @pytest.fixture(scope="function")
# @pytest.fixture(scope="module")
# @pytest.fixture(scope="package")
# @pytest.fixture(scope="session")
def common():
    pass
    # print()
    # print("**"*20)
    # yield "@"
    # print("00"*20) 

def idfn(fixture_value):
    print("--- idfn ---")
    if fixture_value == "aaa":
        return pytest.mark.skip
    else:
        return "spam"


# @pytest.fixture(scope="function")
# @pytest.fixture(scope="class")
@pytest.fixture(scope="module")
# @pytest.fixture(scope="package")
# @pytest.fixture(scope="session")
# @pytest.fixture(scope="module", params=["aaa", "bbb"], ids=[idfn,"ham"])
def common2(request):
    print()
    print("**"*20)
    # print(request.param)
    yield "@"
    print("00"*20) 

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    print(f"--- --- {item.name} {call.when} --- ---")
    # `call`은 호출 결과에 대한 정보를 담고 있는 객체입니다.
    # `when` 인자는 테스트 단계 (`setup`, `call`, `teardown`)을 나타냅니다.
    if call.when == 'call': # when(setup, call, teardown) / reason
        report = pytest.TestReport.from_item_and_call(item, call)
        if report.failed:
            # 실패한 테스트에 대한 커스텀 로직을 작성합니다.
            print(f"Test failed: {item.name}")
            # 예를 들어, 이메일 알림, 로그 기록 등

@pytest.fixture(scope="function")
# @pytest.fixture(scope="class")
# @pytest.fixture(scope="module")
# @pytest.fixture(scope="package")
# @pytest.fixture(scope="session")
def common3():
    print()
    print("##"*20)
    yield "@"
    print("%%%%"*20) 