from abc import ABC, abstractmethod

class Beverage(ABC):
    def prepared_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()
    
    def boil_water(self):
        print("boiling water")
    
    def pour_in_cup(self):
        print("pouring into cup")
    
    @abstractmethod
    def brew(self):
        ...
    
    @abstractmethod
    def add_condiments(self):
        ...

class Tea(Beverage):
    def brew(self):
        print("steeping the tea")
    
    def add_condiments(self):
        print("adding lemon")

class Coffee(Beverage):
    def brew(self):
        print("dripping coffee through filter")
    
    def add_condiments(self):
        print("adding sugar and milk")

if __name__ == "__main__":
    tea = Tea()
    coffee = Coffee()

    print("making tea...")
    tea.prepared_recipe()

    print("making coffee...")
    coffee.prepared_recipe()