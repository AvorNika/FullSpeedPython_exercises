'''3. Create a list comprehension with all the even numbers from 0 to 20, and another
one with all the odd numbers.'''
list_even = [x for x in range(0, 20) if x % 2 == 0]
list_odd = [x for x in range(0, 20) if x % 2 == 1]
print(list_even)
print(list_odd)
