'''5. Make a list comprehension that returns a list with the squares of all even numbers
from 0 to 20, but ignore those numbers that are divisible by 3. In other words,
each number should be divisible by 2 and not divisible by 3. Search for the “and”
keyword in the Python documentation. The resulting list is [4, 16, 64, 100, 196,
256].'''

list1 = [x**2 for x in range(0, 20) if x % 2 == 0 and x % 3 != 0]
print(list1)
