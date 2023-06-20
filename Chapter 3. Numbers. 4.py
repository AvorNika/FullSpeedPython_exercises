'''Use the modulo operator (%) to check which of the following numbers is even or odd:'''
numbers = (1, 5, 20, 60/7)
for num in numbers:
    if num % 2 == 0:
        print(f'The number {num} is even')
    elif num % 2 == 1:
        print(f'The number {num} is odd')
    else:
        print(f'The number {num} is float')
