import time

def saying(interval, what, how_many):
    while how_many > 0:
        time.sleep(interval)
        print(what)
        how_many -= 1

def main():
    print(f"started at {time.strftime('%X')}") 
    saying(1, 'hello', 5)
    saying(2, 'world', 3)
    saying(3, 'python', 2)
    print(f"finished at {time.strftime('%X')}")


main()