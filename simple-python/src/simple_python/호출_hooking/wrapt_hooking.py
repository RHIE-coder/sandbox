import wrapt
import extlib

def beforeInvoked(*args, **kwargs):
    print("call::beforeInvoked()", args, kwargs)

def hook_function(wrapped, instance, args, kwargs):
    print("function call:")
    print("Function:", wrapped)
    print("Args:", args)
    print("Kwargs:", kwargs)
    
    print('-' * 30)
    # beforeInvoked 호출
    beforeInvoked(*args, **kwargs)
    print(dir(wrapped))
    print(wrapped.__name__)
    
    # 원래 함수 호출
    result = wrapped(*args, **kwargs)
    
    # 결과 반환
    print("After function call, result:", result)
    return result


print('before wrapping')
# 이제 extlib.mul이 래핑된 상태에서 호출됩니다.
extlib.mul(20, 30)

print('-' * 30)

# wrapt 사용하여 extlib.mul 함수 래핑 (호출 전에 래핑)
wrapt.wrap_function_wrapper(extlib, 'mul', hook_function)


print('after wrapping')
# 동일하게 래핑된 상태에서 호출됩니다.
extlib.mul(20, 30)
