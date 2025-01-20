# 옵서버 패턴은 들어오는 메서드들을 목록에 저장하는 구독 메서드로 초기 식별할 수 있으며, 만약 위 구독 메서드가 목록의 객체들을 순회하고 그들의 '업데이트' 메서드를 호출하면 해당 패턴은 옵서버 패턴으로 확정지을 수 있습니다.
from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

class ConcreteSubject(Subject):
    _state: int = None

    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an oberser")
        self._observers.append(observer)
    
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
    
    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)
    
    def some_business_logic(self) -> None:
        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just chagned to: {self._state}")
        self.notify()

class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass

class ConcreteObserverA(Observer):
    def update(self, subject:Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")
        

class ConcreteObserverB(Observer):
    def update(self, subject:Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()

