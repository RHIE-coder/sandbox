import mymod
from mymod import MyClass

f1 = getattr(mymod, "myFunc")
f1("hello", "alice")

m = MyClass()
f2 = getattr(m, "my_method")
print(f2(10, 20))