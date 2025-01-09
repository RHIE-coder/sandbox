from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    
    @abstractmethod
    def factory_method(self):
        pass
    
    def some_operation(self) -> str:
        product:Product = self.factory_method()
        
        result = product.operation()
        
        return result

class Product(ABC):
    
    @abstractmethod
    def operation(self) -> str:
        pass
 
class ConcreteProduct1(Product):

    def operation(self) -> str:
        return "result of the ConcreteProduct1"

class ConcreteProduct2(Product):

    def operation(self) -> str:
        return "result of the ConcreteProduct2"

class ConcreteCreator1(Creator):
    
    def factory_method(self) -> Product:
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()

def client_code(creator: Creator) -> None:
    print(f"{creator.some_operation()}")

if __name__ == "__main__":
    client_code(ConcreteCreator1())
    client_code(ConcreteCreator2())