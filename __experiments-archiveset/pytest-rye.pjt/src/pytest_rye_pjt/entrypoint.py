class Test:
    def __init__(self):
        self.hello = "world"
        print("__init__() invoked")

    def __enter__(self):
        print("[enter]")
        return "hey"
    
    def __exit__(self, a, b, c):
        print("[exit]")
        print(a)
        print(b)
        print(c)

    def method(self):
        print("[method]")


def main():
    ...