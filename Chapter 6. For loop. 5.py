'''5. Make the function “is_sorted” that receives a list as parameter and returns True if
the list is sorted in ascending order. For instance [1, 2, 2, 3] is ordered while [1, 2, 3,
2] is not. Suggestion: you have to compare a number in the list with the next one,
so you can use indexes or you need to keep the previous number in a variable as
you iterate over the list.'''


def is_sorted(list1):
    for i in range(len(list1) - 1):
        if list1[i] > list1[i+1]:
            return False
    return True


print(is_sorted([1, 0, 4, 8, 36]))
