# Context:
    # 상태를 관리하고 행동 요청을 위임하는 주요 클래스입니다.
    # 현재 상태를 나타내는 객체를 유지하며, 상태에 따라 요청을 해당 상태 객체에 전달합니다.
# State:
    # 상태를 나타내는 인터페이스나 추상 클래스입니다.
    # 특정 상태에서 Context가 수행할 동작을 정의합니다.
# ConcreteState:
    # State를 구현한 구체적인 클래스들입니다.
    # 각각의 클래스는 Context의 현재 상태에 해당하는 행동을 구현합니다.
from __future__ import annotations
from abc import ABC, abstractmethod

class Context:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    _state = None
    """
    A reference to the current state of the Context 
    """

    def __init__(self, state:State) -> None:
        self.transition_to(state)
    
    def transition_to(self, state:State):
        """
        The Context allows changing the State object at runtime. 
        """
        print(f"Context: Transaction to {type(state).__name__}")
        self._state = state
        self._state.context = self
    
    """
    The Context delegates part of its behavior to the current State object. 
    """
    def request1(self):
        self._state.handle1()
    
    def request2(self):
        self._state.handle2()

class State(ABC):

    @property
    def context(self) -> Context:
        return self._context
    
    @context.setter
    def context(self, context:Context) -> None:
        self._context = context
    
    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass

class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")


class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")

    def handle2(self) -> None:
        print("ConcreteStateB handles requests2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())

if __name__ == "__main__":

    context = Context(ConcreteStateA())
    context.request1()
    context.request2()