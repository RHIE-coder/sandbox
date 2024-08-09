class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
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