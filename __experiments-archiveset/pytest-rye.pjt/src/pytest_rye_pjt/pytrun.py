import pytest
import logging

def caserunner():
    print("----")
    retcode = pytest.main(["-x", "tests"])
    print("----")
    print(retcode)
