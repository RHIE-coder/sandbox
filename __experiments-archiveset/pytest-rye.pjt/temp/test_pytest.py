import pytest
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)

def test_log():

    print()
    print("--"*20)
    print(__name__)
    
    logging.info("This should be printed")
    assert 1 + 1 == 2


def test_console(capfd):
    print("hello")
    captured = capfd.readouterr()
    assert captured.out == "hello\n"

def test_console2(capfd):
    os.system('echo "hello"')
    captured = capfd.readouterr()
    assert captured.out == "hello\n"

def test_example(capsys):
    print("This will be captured.")
    captured = capsys.readouterr()
    assert captured.out == "This will be captured.\n"

# pytest.param("...", value, marks=pytest.mark.xfail)
# @pytest.mark.parametrize("...", [ pytest.param, pytest.param ])
# @pytest.mark.skip
# @pytest.mark.skipif
# @pytest.mark.usefixtures
# @pytest.mark.xfail
# @pytest.fixture