def wrapper(wrapped, instance, args, kwargs):
    print(wrapped)
    print(instance)
    print(args)
    print(kwargs)
    return wrapped(*args, **kwargs)

class Example(object):
    def name(self):
        return 'name'

import wrapt


wrapt.wrap_function_wrapper(Example, 'name', wrapper)

e = Example()
result = e.name()
print(result)