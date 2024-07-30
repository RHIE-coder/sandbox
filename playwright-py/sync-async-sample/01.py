import time

def main():
    print(f"started at {time.strftime('%X')}") 
    print('job A')
    time.sleep(2)
    print('job B')
    time.sleep(2)
    print('job C')
    print(f"finished at {time.strftime('%X')}")


main()