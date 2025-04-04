# 사용자 인터페이스 컴포넌트 간의 통신을 쉽게 하는 것입니다. MVC 패턴의 컨트롤러 부분의 동의어는 중재자입니다.
from __future__ import annotations
from abc import ABC

class Mediator(ABC):
    def notify(self, sender: object, event: str) -> None:
        pass

class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2:Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self
    
    def notify(self, sender: object, event:str) -> None:
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()
        
class BaseComponent:
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator
    
    @property
    def mediator(self) -> Mediator:
        return self._mediator
    
    @mediator.setter
    def mediator(self, mediator:Mediator) -> None:
        self._mediator = mediator
    
class Component1(BaseComponent):
    def do_a(self) -> None:
        print("Component 1 does A")
        self.mediator.notify(self, "A")
    
    def do_b(self) -> None:
        print("Component 1 does B")
        self.mediator.notify(self, "B")

class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Component 2 does C")
        self.mediator.notify(self, "C")
    
    def do_d(self) -> None:
        print("Component 2 does D")
        self.mediator.notify(self, "D")

if __name__ == "__main__":
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)
    
    print("Client triggers operation A")
    c1.do_a()

    print()

    print("Client triggers operation D")
    c2.do_d()
        

