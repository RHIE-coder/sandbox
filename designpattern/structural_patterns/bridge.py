from abc import ABC, abstractmethod

class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass

class Abstraction:
    
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation
    
    def operation(self) -> str:
        return (f"Abstract: base operation: {self.implementation.operation_implementation()}")

class ExtendedAbstraction(Abstraction):
    
    def operation(self) -> str:
        return (f"ExtendedAbstraction: extended operation: {self.implementation.operation_implementation()}")

class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "impl from platfrom A"

class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "impl from platfrom B"
    
def client_code(abstraction: Abstraction) -> None:
    print(abstraction.operation())

if __name__ == "__main__":
    
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    implementaion = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)