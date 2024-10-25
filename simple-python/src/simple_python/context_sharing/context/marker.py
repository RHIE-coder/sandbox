from typing import Callable
from functools import wraps
from .box import lazy
from pprint import pprint as pp

def mark(*, deps=None):
    def decorator(func:Callable):
        func.deps = deps
        lazy.add(func.__module__, func.__name__)

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    return decorator