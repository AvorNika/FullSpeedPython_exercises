'''2. Change the previous program to schedule the execution of two calls to the sum
function.'''

import asyncio


async def add_nums(x, y):
    sum_nums = x + y
    await asyncio.sleep(sum_nums)
    return sum_nums


async def when_done(tasks):
    for res in asyncio.as_completed(tasks):
        print('Result:', await res)


loop = asyncio.get_event_loop()

loop.run_until_complete(when_done([
    add_nums(4, 3),
    add_nums(2, 1)
]))

loop.close()
