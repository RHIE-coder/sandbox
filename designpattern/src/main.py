from collections.abc import Callable

def decorator(desc:str, cb:Callable):
    def func_receiver(func):
        def wrapper(*args, **kwargs):
            func.desc = desc
            cb(desc)
            return func(*args, **kwargs)
        return wrapper
    return func_receiver


class Wraps:

    @decorator("aaa")
    @staticmethod
    def TC_A():
        print("testcase A")
    

    @decorator("bbb")
    @staticmethod
    def TC_B():
        print("testcase B")

    @decorator("ccc", cb=Wraps.TC_B)
    @staticmethod
    def TC_C():
        print("testcase C")

