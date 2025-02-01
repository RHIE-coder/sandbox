from __future__ import annotations
from abc import ABC, abstractmethod 

class ChatMediator(ABC):
    def send_message(self, message:str, user:User):
        ...
    def add_user(user:User):
        ...

class ClassMediatoreImpl(ChatMediator):
    users:list[User]
    
    def __init__(self):
        self.users = list()
    
    def add_user(self, user:User):
        self.users.append(user)
    
    def send_message(self, message:str, user:User):
        for u in self.users:
            if u != user:
                u.receive(message)

class User:
    mediator:ChatMediator
    name:str

    def __init__(self, mediator:ClassMediatoreImpl, name:str):
        self.mediator = mediator
        self.name =name 
        self.mediator.add_user(self)
    
    def send(self, message:str):
        self.mediator.send_message(message, self)
    
    def receive(self, message:str):
        print(f"{self.name} receive message: {message}")

if __name__ == "__main__":
    mediator = ClassMediatoreImpl()

    u1 = User(mediator, "AAA")
    u2 = User(mediator, "BBB")
    u3 = User(mediator, "CCC")
    u4 = User(mediator, "DDD")

    u1.send("Hello World")