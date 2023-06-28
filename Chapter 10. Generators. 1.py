'''1. Implement a generator called “squares” to yield the square of all numbers from (a)
to (b). Test it with a “for” loop and print each of the yielded values.'''


def squares(a, b):
    while a < b:
        yield a ** 2
        a += 1


for value in squares(1, 8):
    print(value)
