'''1. Find the greatest common divisor of the following pairs of numbers: (15, 21), (152,
200), (1988, 9765).'''
import math
numbers = ((15, 21), (152, 200), (1988, 9765))
for nums in numbers:
    print(math.gcd(nums[0], nums[1]))
    