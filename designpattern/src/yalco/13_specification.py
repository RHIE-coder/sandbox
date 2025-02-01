from abc import ABC, abstractmethod
from collections.abc import Callable

class Specification(ABC):
    @abstractmethod
    def is_satisfied_by(self, number:int):
        ...
    def conjoin(self, other:"Specification") -> "Specification":
        return LambdaSpecification(
            lambda number: self.is_satisfied_by(number) \
            and other.is_satisfied_by(number)
        )

class LambdaSpecification(Specification):
    def __init__(self, predication: Callable[[int], bool]):
        self.__predication = predication
    
    def is_satisfied_by(self, number:int) -> bool:
        return self.__predication(number)

class EvenSpecification(Specification):

    def is_satisfied_by(self, number):
        return number % 2 == 0

class RangeSpecification(Specification):
    __min:int
    __max:int

    def __init__(self, min:int, max:int):
        self.__min = min
        self.__max = max
    
    def is_satisfied_by(self, number):
        return number >= self.__min and number <= self.__max

    
if __name__ == "__main__":
    even_spec:Specification = EvenSpecification()
    range_spec:Specification = RangeSpecification(10, 20)

    even_and_range_spec:Specification = even_spec.conjoin(range_spec)

    number = 24

    print(f"Even: {even_spec.is_satisfied_by(number)}")
    print(f"In range 10-20: {range_spec.is_satisfied_by(number)}")
    print(f"Even and in range 10-20: {even_and_range_spec.is_satisfied_by(number)}")

    number = 12

    print(f"Even: {even_spec.is_satisfied_by(number)}")
    print(f"In range 10-20: {range_spec.is_satisfied_by(number)}")
    print(f"Even and in range 10-20: {even_and_range_spec.is_satisfied_by(number)}")