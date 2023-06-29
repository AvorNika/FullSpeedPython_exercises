'''1. Create a coroutine named “square” that prints the square of any sent value.'''


def coroutine():
    print('This coroutine prints the square of any sent value')
    while True:
        val = yield
        print(f'Square {val} is {val**2}')


co = coroutine()
next(co)
co.send(1)
co.send(10)
