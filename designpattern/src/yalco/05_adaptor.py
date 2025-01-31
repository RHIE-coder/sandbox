from abc import ABC, abstractmethod

# Target Interface
class ModernMessageSender(ABC):
    @abstractmethod
    def send_message(self, message:str, recipient:str):
        ...

# Adaptee Interface
class OldMessageSender(ABC):
    @abstractmethod
    def send(self, message_data:list[str]):
        ...

class OldMessageSystem(OldMessageSender):
    def send(self, message_data:list[str]):
        print(f"OldMessageSystem: Sending message: {message_data[0]} to {message_data[1]}")
        return 1

class MessageAdapter(ModernMessageSender):
    __old_system:OldMessageSender

    def __init__(self, old_system:OldMessageSender):
        self.__old_system = old_system
    
    def send_message(self, message:str, recipient:str):
        message_data:list[str] = [message, recipient]

        result = self.__old_system.send(message_data)

        if result != 1:
            print("fail to send message")

if __name__ == "__main__":
    old_system:OldMessageSender = OldMessageSystem()
    adapter:ModernMessageSender = MessageAdapter(old_system)

    adapter.send_message("Hello World", "rhie@example.com")