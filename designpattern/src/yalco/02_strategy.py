from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount:int):
        ...

class CreditCardPayment(PaymentStrategy):
    __name:str
    __card_number:str

    def __init__(self, name, card_number):
        self.__name = name
        self.__card_number = card_number
    
    def pay(self, amount:int):
        print(f"신용카드를 활용하여 {amount}원을 결제하였습니다.")
        print(f"카드정보(이름={self.__name}, 카드번호={self.__card_number})")

class PayPalPayment(PaymentStrategy):
    __email:str

    def __init__(self, email:str):
        self.__email = email
    
    def pay(self, amount:int):
        print(f"페이팔을 활용하여 {amount}원을 결제하였습니다")
        print(f"결제 영수증은 {self.__email}로 보냈습니다.")

    
class ShoppingCart: # Context
    __payment_strategy:PaymentStrategy

    def set_payment_method(self, payment_strategy:PaymentStrategy):
        self.__payment_strategy = payment_strategy
    
    def checkout(self, amount:int):
        self.__payment_strategy.pay(amount)

if __name__ == "__main__":
    cart = ShoppingCart()

    cart.set_payment_method(CreditCardPayment("RHIE", "123123123"))
    cart.checkout(111)

    cart.set_payment_method(PayPalPayment("rhie@example.com"))
    cart.checkout(222)



    