from threading import Lock, Thread

class SingletonMeta(type):
    
    _instances = {}
    _lock: Lock = Lock()
    
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]
    
class Singleton(metaclass=SingletonMeta):

    value: str = None
    
    def __init__(self, value: str) -> None:
        self.value = value
        
    def some_biz_logic(self):
        ...
    
class Singleton2(metaclass=SingletonMeta):

    value: str = None
    
    def __init__(self, value: str) -> None:
        self.value = value

    def some_biz_logic2(self):
        ...

if __name__ == "__main__":
    
    s1 = Singleton(1)
    s2 = Singleton(2)
    
    print(id(s1) == id(s2))
    
    ss1 = Singleton2(11)
    ss2 = Singleton2(22)
    
    print(id(ss1) == id(ss2))
    
    print(SingletonMeta._instances)

    
## OUTPUT
"""
True
True
{
    <class '__main__.Singleton'>: <__main__.Singleton object at 0x100563f50>,
    <class '__main__.Singleton2'>: <__main__.Singleton2 object at 0x100563f80>
}
"""




