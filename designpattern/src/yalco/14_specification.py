from abc import ABC, abstractmethod 
from dataclasses import dataclass
from typing import TypeVar, Generic
from rich.console import Console
console = Console()

T = TypeVar("T")


class Specification(ABC, Generic[T]):
    @abstractmethod
    def is_satisfied_by(self, item:T)->bool:
        ...



class AndSpec(Specification[T]):
    __spec1:Specification[T]
    __spec2:Specification[T]

    def __init__(self, spec1:Specification[T], spec2:Specification[T]):
        self.__spec1 = spec1
        self.__spec2 = spec2
    
    def is_satisfied_by(self, item:T)->bool:
        return (
            self.__spec1.is_satisfied_by(item)
            and
            self.__spec2.is_satisfied_by(item)
        )

class NotSpec(Specification[T]):
    __spec:Specification[T]

    def __init__(self, spec:Specification[T]):
        self.__spec = spec
    
    def is_satisfied_by(self, item:T)->bool:
        return not self.__spec.is_satisfied_by(item)
        
class OrSpec(Specification[T]):
    __spec1:Specification[T]
    __spec2:Specification[T]

    def __init__(self, spec1:Specification[T], spec2:Specification[T]):
        self.__spec1 = spec1
        self.__spec2 = spec2
    
    def is_satisfied_by(self, item:T)->bool:
        return (
            self.__spec1.is_satisfied_by(item)
            or
            self.__spec2.is_satisfied_by(item)
        )
        
@dataclass(frozen=True)
class Product:
    name: str
    category: str
    price: int
    stock: int
        

class CategorySpec(Specification):
    __category:str

    def __init__(self, category:str):
        self.__category = category
    
    def is_satisfied_by(self, item:"Product")->bool:
        return item.category == self.__category

class PriceSpec(Specification):
    __max_price:int
    
    def __init__(self, max_price):
        self.__max_price = max_price
    
    def is_satisfied_by(self, item:"Product")->bool:
        return item.price <= self.__max_price

class InStockSpec(Specification):
    
    def is_satisfied_by(self, item:"Product")->bool:
        return item.stock > 0
    
if __name__ == "__main__":
    products: list[Product] = [
        Product("Labtop", "Electronics", 1200, 5),
        Product("SmartPhone", "Electronics", 800, 0),
        Product("HeadPhones", "Electronics", 200, 10),
        Product("Book", "Literature", 20, 50),
    ]
    
    elec_spec = CategorySpec("Electronics")
    stock_spec = InStockSpec()
    expected_price_spec = PriceSpec(500)

    elec_and_stock = AndSpec(elec_spec, stock_spec)
    elec_or_stock = OrSpec(elec_spec, stock_spec)
    not_expected_price = NotSpec(expected_price_spec)

    console.print(
        [prod for prod in products if elec_and_stock.is_satisfied_by(prod)]
    )
    print("*" * 50)

    console.print(
        [prod for prod in products if elec_or_stock.is_satisfied_by(prod)]
    )
    print("*" * 50)

    console.print(
        [prod for prod in products if not_expected_price.is_satisfied_by(prod)]
    )