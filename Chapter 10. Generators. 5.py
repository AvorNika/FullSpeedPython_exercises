'''5. Create a generator to return the fibonnaci sequence starting from the first element
up to (n). The first numbers of the sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
89, . . .'''


def fib_nums(n):
    f0 = 0
    f1 = 1
    while n > 0:
        yield f0
        f1, f0 = f0 + f1, f1
        n -= 1


for num in fib_nums(20):
    print(num)
