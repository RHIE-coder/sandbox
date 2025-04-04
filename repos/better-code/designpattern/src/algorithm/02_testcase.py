from rich.console import Console
from collections.abc import Callable
from typing import Generic, TypeVar
from collections import defaultdict

console = Console()

T = TypeVar('T')

from functools import wraps

def invoker(*,
    precondition
):
    def decorator(func):
        func.pre = precondition

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

class Singleton(type, Generic[T]):
    __instances = {} 

    def __call__(cls, *args, **kwargs) -> T:
        console.print("[blue] Singleton invoked [/blue]")
        if cls not in cls.__instances:
            console.print("[yellow] found out not allocated yet[/yellow]")
            cls.__instances[cls] = super().__call__(*args, **kwargs)
            console.print("[green] allocated ! [/green]")

        return cls.__instances[cls]

    @staticmethod
    def get_instance(cls):
        return Singleton.__instances.get(cls, None) 

class PreconditionBroker(metaclass=Singleton):

    __preconditions:dict
    
    def __init__(self):
        self.__preconditions = dict() 

class Test:
    @staticmethod
    def ttt1():
        print("ttt1")
        return True




def ok_precond_1():
    console.print("[green]Executing OK Precondition 1[/green]")
    return True  

def ok_precond_2():
    console.print("[green]Executing OK Precondition 2[/green]")
    return True  

def ok_precond_3():
    console.print("[green]Executing OK Precondition 3[/green]")
    return True  

def fail_precond_1():
    console.print("[red]Executing FAIL Precondition 1[/red]")
    return False

def fail_precond_2():
    console.print("[red]Executing FAIL Precondition 2[/red]")
    return False 

def main():
    ...
    console.print(Singleton.check(PreconditionManager)) # None

    p1 = PreconditionManager()
    p2 = PreconditionManager()
    p3 = PreconditionManager()
    p4 = PreconditionManager()
    p5 = PreconditionManager()

    console.print(id(p1))
    console.print(id(p2))
    console.print(id(p3))
    console.print(id(p4))
    console.print(id(p5))

    console.print(Singleton.check(PreconditionManager)) # Still None ---> Why?


if __name__ == "__main__":
    main()