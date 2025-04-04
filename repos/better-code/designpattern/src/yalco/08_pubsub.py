class Message:
    __content:str
    __topic:str

    def __init__(self, content:str, topic:str):
        self.__content = content
        self.__topic = topic
    
    @property
    def content(self)->str:
        return self.__content
    
    @property
    def topic(self)->str:
        return self.__topic

##############################
from abc import ABC, abstractmethod

class Publisher(ABC):
    @abstractmethod
    def publish(message:Message):
        ...

class Subscriber(ABC):
    @abstractmethod
    def update(message:Message):
        ...

##############################
from collections.abc import Mapping
from collections import defaultdict

class Broker:
    __subscribers:Mapping[str, list[Subscriber]] = defaultdict(list)

    def subscribe(self, topic:str, subscriber:Subscriber):
        self.__subscribers[topic].append(subscriber)
    
    def publish(self, message:Message):
        topic_subscriber: list[Subscriber] = self.__subscribers.get(message.topic)

        if topic_subscriber is not None:
            for subscriber in topic_subscriber:
                subscriber.update(message)

class NewsPublisher(Publisher):
    __broker:Broker

    def __init__(self, broker:Broker):
        self.__broker = broker
    
    def publish(self, message:Message):
        print(f"Publishing {message.content} on topic {message.topic}")
        self.__broker.publish(message)

class NewsSubscriber(Subscriber):
    __name:str

    def __init__(self, name:str):
        self.__name = name
    
    def update(self, message:Message):
        print(f"{self.__name} received: {message.content} on topic: {message.topic}")

if __name__ == "__main__":
    broker:Broker = Broker()

    publisher:NewsPublisher = NewsPublisher(broker)

    subscriber1:NewsSubscriber = NewsSubscriber('Subscriber 1')
    subscriber2:NewsSubscriber = NewsSubscriber('Subscriber 2')

    broker.subscribe("sports", subscriber1)
    broker.subscribe("weather", subscriber2)
    broker.subscribe("sports", subscriber2)

    publisher.publish(Message("스포츠 결승 경기가 시작되었습니다", "sports"))
    publisher.publish(Message("오늘 날씨는 화창합니다", "weather"))
