def func():
    ...

class Prop:
    ...


# func[Prop] = "hello" # TypeError: 'function' object does not support item assignment
# print(func[Prop])

func.a = "hello"
print(func.a)

# setattr(func, Prop, "hello") # TypeError: attribute name must be string, not 'type'
# print(getattr(func, Prop))

print(type(func.a)) # <class 'str'>
print(type("hello") == str) # true