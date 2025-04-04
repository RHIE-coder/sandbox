from rich.console import Console
console = Console()

import pytest

@pytest.mark.parametrize("case", ["normal", "blocked"])
def test_example(case):
    """BLOCKED 상태 테스트"""
    if case == "blocked":
        pytest.xfail("🚧 BLOCKED 테스트입니다!")  # XFAILED 처리 (BLOCKED로 변경될 것)
    assert case == "normal"
def AAA(k=BBB):
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