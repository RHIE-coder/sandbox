import pytest
from rich.console import Console
console = Console()
# ✅ BLOCKED 상태를 저장하는 딕셔너리
blocked_tests = set()

# @pytest.hookimpl(tryfirst=True)
# def pytest_runtest_logreport(report):
#     """테스트 실행 중 특정 테스트를 BLOCKED 상태로 분류"""
#     if report.when == "call" and "blocked" in report.nodeid:
#         blocked_tests.add(report.nodeid)
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    if report.when == "call" and "blocked" in report.nodeid:
        blocked_tests.add(report.nodeid)
    
    console.log(blocked_tests)




@pytest.hookimpl(tryfirst=True)
def pytest_report_teststatus(report, config):
    console.log("이것은 출력이 되는 것인가")
    """BLOCKED 상태 추가"""
    if report.when == "call" and report.nodeid in blocked_tests:
        return "blocked", "B", "BLOCKED"
    

console.log("LOAD CONFTEST")

def AAA():
    print("AAA")
    CCC()
    ...

def BBB():
    print("BBB")
    CCC()
    ...

def CCC():
    print("CCC")
    ...

AAA()
