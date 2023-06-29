'''2. Implement the “minimize” coroutine that keeps and prints the minimum value that
is sent to the function.'''


def minimize():
    result = []
    print('This coroutine prints the minimum value that is sent to the function')
    while True:
        val = yield
        result.append(val)
        print(f'Minimum value is {min(result)}')


mini = minimize()
next(mini)
mini.send(4)
mini.send(6)
