import pytest

@pytest.fixture
def hello(test_common):
    print(" >>> hello")
    print(test_common)
    return "hello"

@pytest.fixture
def world():
    print(" >>> world")
    return "world"

@pytest.fixture
def aaa(hello):
    print("--- aaa ---")
    print(hello)
    return "hhhh"

@pytest.fixture
def bbb(hello, world, aaa):
    print("--- bbb ---")
    print(hello)
    print(world)
    print(aaa)
    return "HHH"

# ERROR
# def test_accept_data2(take_my_data):
#     print(take_my_data)
#     assert take_my_data == 10

def test_here(bbb):
    assert bbb == "HHH"