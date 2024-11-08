import sys
import extlib

def trace_calls(frame, event, arg):
    if event == 'call':
        funcnm = frame.f_code.co_name
        print(f"Calling function: {funcnm}")
        beforeInvoked()  
    return trace_calls #계속 추적하기 위해

def beforeInvoked(*args, **kwargs):
    print("call::beforeInvoked()", args, kwargs)

sys.settrace(trace_calls)

extlib.add(10, 20)

sys.settrace(None)

extlib.mul(10, 20)