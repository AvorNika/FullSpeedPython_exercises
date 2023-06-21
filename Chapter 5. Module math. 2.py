'''2. Compute the base-2 logarithm of the following numbers: 0, 1, 2, 6, 9, 15.'''
import math
numbers = (0, 1, 2, 6, 9, 15)
for num in numbers:
    if num > 0:
        print(math.log2(num))
