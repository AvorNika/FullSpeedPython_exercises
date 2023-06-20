'''4. Create a list with the squares of the even numbers from 0 to 20, and sum the list
using the “sum” function. The result should be 1140. First create the list using list
comprehensions, check the result, then apply the sum to the list comprehension.'''

list1 = [x**2 for x in range(0, 20) if x % 2 == 0]
print(list1)
print(sum(list1))
