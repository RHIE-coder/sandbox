class TestClassDemoInstance:
    value = 0

    def __init__(self, test_common):
        print("--"*20)
        print("TestClassDemoInstance.__init__()")
        print(test_common)


    def test_one(self, test_common):
        self.value = 1
        print("--"*20)
        print("test_one()")
        print(test_common)
        assert self.value == 1

    def test_two(self):
        assert self.value == 1

class TestClassDemoInstance:
    value = 0

    def test_one(self):
        TestClassDemoInstance.value = 1
        assert TestClassDemoInstance.value == 1

    def test_two(self):
        assert TestClassDemoInstance.value == 1