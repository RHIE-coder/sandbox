from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount:int):
        ...

class CreditCardPayment(PaymentStrategy):
    __name:str
    __card_number:int

    def __init__(self, name, card_number):
        self.__name = name
        self.__card_number = card_number

    def pay(self, amount:int):
        print(f"{amount} paid with credit card")
        print(f"card number is {self.__card_number}, and name is {self.__name}")

class PayPalPayment(PaymentStrategy):
    __email:str

    def __init__(self, email):
        self.__email = email

    def pay(self, amount:int):
        print(f"{amount} paid with paypal")
        print(f"the receipt sent to {self.__email}")

class ShoppingCart:
    __payment_strategy:PaymentStrategy

    def set_payment_strategy(self, payment_strategy:PaymentStrategy):
        self.__payment_strategy = payment_strategy

    def checkout(self, amount:int):
        self.__payment_strategy.pay(amount) 