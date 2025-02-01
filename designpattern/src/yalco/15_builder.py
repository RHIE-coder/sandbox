from dataclasses import dataclass
from typing import Type

def builder(cls: Type["Product"]) -> Type["Product"]:
    """클래스에 빌더 패턴을 자동 추가하는 데코레이터"""
    class Builder:
        def __init__(self):
            self._name = None
            self._category = None
            self._price = None
            self._stock = None

        def set_name(self, name: str) -> "Builder":
            self._name = name
            return self

        def set_category(self, category: str) -> "Builder":
            self._category = category
            return self

        def set_price(self, price: int) -> "Builder":
            self._price = price
            return self

        def set_stock(self, stock: int) -> "Builder":
            self._stock = stock
            return self

        def build(self) -> "Product":
            return cls(self._name, self._category, self._price, self._stock)

    cls.builder = lambda: Builder()  # 정적 메서드로 `builder()` 추가
    return cls

@builder
@dataclass(frozen=True)
class Product:
    name: str
    category: str
    price: int
    stock: int

product = (
    Product.builder()
    .set_name("Laptop")
    .set_category("Electronics")
    .set_price(1500)
    .set_stock(10)
    .build()
)

print(product) # Product(name='Laptop', category='Electronics', price=1500, stock=10)
print(type(product)) # Product