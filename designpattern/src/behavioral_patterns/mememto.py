# 이 패턴은 객체 상태의 스냅숏을 만든 후 나중에 복원할 수 있도록 합니다.
# Originator:
    # 저장될 상태를 가지고 있는 객체.
# Memento:
    # Originator의 상태를 캡처하고 저장하는 객체.
    # 저장된 상태는 외부에서 수정되지 않도록 보호.
# Caretaker:
    # Memento 객체를 관리하며, 필요할 때 상태를 복원.
from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters
from typing import List

class Originator:

    _state = None

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: My initial state is: {self._state}")
    
    def do_something(self) -> None:
        print("Originator: I'm doing something important")
        self._state = self._generate_random_string(30)
    
    @staticmethod
    def _generate_random_string(length:int = 10) -> str:
        return "".join(sample(ascii_letters,length))
    
    def save(self) -> Mememto:
        return ConcreteMememto(self._state)
    
    def restore(self, mememto: Mememto) -> None:
        self._state = mememto.get_state()
        print(f"Originator: My state has changed to: {self._state}")


class Mememto(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass

class ConcreteMememto(Mememto):
    def __init__(self, state:str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19] # 2025-01-20 15:49:50.604999 --> 2025-01-20 15:50:04
    
    def get_state(self) -> str:
        return self._state
    
    def get_name(self) -> str:
        return f"{self._date} / ({self._state[0:9]}...)"
    
    def get_date(self) -> str:
        return self._date

class Caretaker:
    def __init__(self, originator: Originator) -> None:
        self._mememtos: List[Mememto] = []
        self._originator = originator
    
    def backup(self) -> None:
        print("Caretake: Saving Originator's state...")
        self._mememtos.append(self._originator.save())
    
    def undo(self) -> None:
        if not len(self._mememtos):
            return
        
        mememto = self._mememtos.pop()
        print(f"Caretaker: Restoring state to: {mememto.get_name()}")
        try:
            self._originator.restore(mememto)
        except Exception:
            self.undo()
    
    def show_history(self) -> None:
        print("Caretaker: Here's the list of mememtos:")
        for mememto in self._mememtos:
            print(mememto.get_name())

if __name__ == "__main__":
    originator = Originator("Super-duper-super-puper-super.")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()

    print("\nClient: Now, let's rollback!\n")
    caretaker.undo()

    print("\nClient: Once more!\n")
    caretaker.undo()