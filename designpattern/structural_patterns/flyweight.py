import json
from typing import Dict

class Flyweight():
    def __init__(self, shared_state:str) -> None:
        self._shared_state = shared_state
    
    def operation(self, unique_state:str) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.")
    
class FlyweightFactory():

    _flyweights: Dict[str, Flyweight] = {}
    
    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)
    
    def get_key(self, state: Dict) -> str:
        return "_".join(sorted(state))
    
    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        key = self.get_key(shared_state)
    
def add_car_to_police_database(
    factory: FlyweightFactory,
    plates: str,
    owner: str,
    brand: str,
    model: str,
    color: str,
):
    ...

if __name__ == "__main__":
    scores = {'332': 90, '2134': 75, '12345': 85}
    print(sorted(scores))