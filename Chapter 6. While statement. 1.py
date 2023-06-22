'''1. Implement a function that receives a number as parameter and prints, in decreasing
order, which numbers are even and which are odd, until it reaches 0.'''


def even_odd(n):
    for i in range(n, 0, -1):
        if i % 2 == 0:
            print('Even number:', i)
        if i % 2 == 1:
            print('Odd number:', i)


even_odd(int(input()))
