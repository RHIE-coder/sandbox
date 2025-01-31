from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def interpret(self):
        ...

class Number(Expression):
    __number:int

    def __init__(self, num:int):
        self.__number = num
    
    def interpret(self):
        return self.__number
    
class Add(Expression):
    __left_expr:Expression
    __right_expr:Expression

    def __init__(self, left, right):
        self.__left_expr = left
        self.__right_expr = right
    
    def interpret(self):
        return self.__left_expr.interpret() + self.__right_expr.interpret()
    
class Subtract(Expression):
    __left_expr:Expression
    __right_expr:Expression

    def __init__(self, left, right):
        self.__left_expr = left
        self.__right_expr = right
    
    def interpret(self):
        return self.__left_expr.interpret() - self.__right_expr.interpret()

if __name__ == "__main__":
    # (5+2)-3
    five:Expression = Number(5)
    two:Expression = Number(2)
    three:Expression = Number(3)

    add_expr:Expression = Add(five, two)

    sub_expr:Expression = Subtract(add_expr, three)

    print(f"(5+2)-3 = {sub_expr.interpret()}")