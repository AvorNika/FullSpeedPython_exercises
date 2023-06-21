'''1. Implement the factorial function and test it with several different values. Cross-check
with a calculator.'''


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(5))
