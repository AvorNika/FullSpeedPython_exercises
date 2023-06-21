'''1. Implement the “add2” function that receives two numbers as arguments and returns
the sum of the numbers. Then implement the “add3” function that receives and
sums 3 parameters.'''
n1, n2, n3 = int(input()), int(input()), int(input())


def add2(num1, num2):
    return num1 + num2


def add3(num1, num2, num3):
    return num1 + num2 + num3


print(add2(n1, n2))
print(add3(n1, n2, n3))
