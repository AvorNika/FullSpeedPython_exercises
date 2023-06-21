'''2. Implement a recursive function to compute the sum of the (n) first integer numbers
(where (n) is a function parameter). Start by thinking about the base case (the sum
of the first 0 integers is?) and then think about the recursive case.'''
n = int(input())


def sum_nums(x):
    if x == 0:
        return 0
    else:
        return x + sum_nums(x - 1)


print(sum_nums(n))
