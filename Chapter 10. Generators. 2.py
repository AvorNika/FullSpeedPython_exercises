'''2. Create a generator to yield all the even numbers from 1 to (n).'''


def even_nums(n):
    x = 1
    while x < n:
        if x % 2 == 0:
            yield x
        x += 1


for num in even_nums(26):
    print(num)
