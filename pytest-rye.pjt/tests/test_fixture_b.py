import pytest

@pytest.fixture
def take_my_data():
    return 10

def test_accept_data(take_my_data):
    print()
    print(take_my_data)
    assert take_my_data == 10