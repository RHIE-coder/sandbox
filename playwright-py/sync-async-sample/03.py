import asyncio
import time

async def saying(interval, what, how_many):
    while how_many > 0:
        await asyncio.sleep(interval)
        print(what)
        how_many -= 1

async def main():
    coro1 =  saying(1, 'hello', 5)
    coro2 =  saying(2, 'world', 3)
    coro3 =  saying(3, 'python', 2)
    print(f"started at {time.strftime('%X')}") 
    await asyncio.gather(
        coro1, coro2, coro3
    )
    print(f"finished at {time.strftime('%X')}")

# asyncio.run(main())
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()