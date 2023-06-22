'''The Fibonnaci sequence is a sequence of numbers in which each number of the
sequence matches the sum of the previous two terms. Given the following recursive
definition implement (fib(n)). Check your results for the first numbers of the sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21,
34, 55, 89, . . .'''
x = int(input())


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(x))
