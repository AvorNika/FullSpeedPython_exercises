'''4. Implement a function that returns the reverse of a list received as parameter.
You may create an empty list and keep adding the values in reversed order as
they come from the original list.'''


def reverse_func(list1, list2):
    for i in range(-1, -(len(list1) + 1), -1):
        list2.append(list1[i])
    return list2


print(reverse_func([1, 5, 9, 3, 5, 6], []))
