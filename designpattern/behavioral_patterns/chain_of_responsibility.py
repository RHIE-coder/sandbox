from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler(ABC):
    @abstractmethod
    def set_next(self, handeer:Handler) -> Handler:
        pass

    
    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass

class AbstractHandler(Handler):
    _next_handler : Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler
    
    @abstractmethod
    def handle(self, request:Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        
        return None
    

class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)

class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)

class DogHandler(AbstractHandler):
    def handle(self, request:Any) -> str:
        if request == "MetaBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)

def client_code(handler:Handler) -> None:
    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"Client: who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}")
            print(f"  {food} was left untouched")
        else:
            print("  silence...")
        print()

if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)

    print("Subchain: Squirrel > Dog")
    client_code(squirrel)