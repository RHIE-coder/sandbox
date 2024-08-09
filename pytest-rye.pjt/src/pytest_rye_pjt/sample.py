# from pytest_rye_pjt import justdoit
from pytest_rye_pjt.justdoit import *
 

# @justdoit.JustDoIt([1,2,3,4,5,6,7,8,9,10])
@JustDoIt([1,2,3,4,5,6,7,8,9,10])
def result(*, do):
    return f"just do it : {do}"

def main():
    test = [1,2,3,4,5]
    print(f"jsut: {test}")
    output1 = result(do="sum")
    output2 = result(do="max")
    output3 = result(do="nothing")

    print(output1)
    print(output2)
    print(output3)