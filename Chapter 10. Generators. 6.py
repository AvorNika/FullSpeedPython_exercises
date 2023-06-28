'''6. Implement a generator that returns all consecutive pairs of numbers from 0 to (n),
such as (0, 1), (1, 2), (2, 3). . .'''


def pairs(n):
    x = 0
    while x < n:
        yield x, x+1
        x += 1


for pair in pairs(20):
    print(pair)
