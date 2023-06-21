'''2. Implement a function that returns the greatest of two numbers given as parameters.
Use the “if” statement to compare both numbers.'''
n1, n2 = int(input()), int(input())


def max_num(num1, num2):
    if num1 > num2:
        return num1
    elif num1 == num2:
        return "The numbers are equal"
    else:
        return num2


print(max_num(n1, n2))
