'''1. Implement an asynchronous coroutine function to add two variables and sleep for
the duration of the sum. Use the asyncio loop to call the function with two numbers.'''
import asyncio


async def add_nums(x, y):
    sum_nums = x + y
    await asyncio.sleep(sum_nums)
    return sum_nums


loop = asyncio.get_event_loop()

results = loop.run_until_complete(add_nums(2, 3))
print(results)

loop.close()
