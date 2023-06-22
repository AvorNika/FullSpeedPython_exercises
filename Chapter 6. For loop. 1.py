'''1. Create a function “add” that receives a list as parameter and returns the sum of all
elements in the list. Use the “for” loop to iterate over the elements of the list.'''


def add(list1):
    sum1 = 0
    for elem in list1:
        sum1 += elem
    return sum1


print(add([0, 5, 8, 9, 134, 45]))
