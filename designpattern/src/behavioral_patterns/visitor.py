# Visitor:
    # 방문자를 표현하는 인터페이스 또는 추상 클래스.
    # 객체 구조의 각 요소를 방문하는 메서드를 정의.
# ConcreteVisitor:
    # 실제 방문자를 구현.
    # 요소를 방문하며 구체적인 동작을 수행.
# Element:
    # 방문 대상이 되는 객체의 인터페이스 또는 추상 클래스.
    # 방문자(Visitor)를 받아들이는 메서드(accept)를 정의.
# ConcreteElement:
    # 실제로 방문 가능한 요소를 구현.
    # 각 요소는 accept 메서드에서 Visitor를 호출하여 자신의 상태를 전달.
# Object Structure:
    # 여러 Element 객체로 구성된 객체 구조.
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Component(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

class ConcreteComponentA(Component):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_component_a(self)
    
    def exclusive_method_of_concrete_component_a(self) -> str:
        return "A"

class ConcreteComponentB(Component):
    def accept(self, visitor: Visitor):
        visitor.visit_concrete_component_b(self)

    def special_method_of_concrete_component_b(self) -> str:
        return "B"

class Visitor(ABC):
    @abstractmethod
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        pass

class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element:Component):
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor1")
    
    def visit_concrete_component_b(self, element:Component):
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor1")

class ConcreteVisitor2(Visitor):
    def visit_concrete_component_a(self, element:Component):
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor2")

    def visit_concrete_component_b(self, element:Component):
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor2")

def client_code(components: List[Component], visitor: Visitor) -> None:
    for component in components:
        component.accept(visitor)

if __name__ == "__main__":
    components = [ConcreteComponentA(), ConcreteComponentB()]

    print("The client code works with all visitors via the base Visitor interface")
    visitor1 = ConcreteVisitor1()
    client_code(components, visitor1)

    visitor2 = ConcreteVisitor2()
    client_code(components, visitor2)