'''3. Implement a function named “is_divisible” that receives two parameters (named “a”
and “b”) and returns true if “a” can be divided by “b” or false otherwise. A number
is divisible by another when the remainder of the division is zero. Use the modulo
operator (“%”).'''
num1, num2 = int(input()), int(input())


def is_divisible(a, b):
    return a % b == 0


print(is_divisible(num1, num2))
