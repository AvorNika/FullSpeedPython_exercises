'''7. Implement the “has_duplicates” function which verifies if a list has duplicate values.
You may have to use two “for” loops, where for each value you have to check for
duplicates on the rest of the list.'''


def has_duplicates(list1):
    for i in range(len(list1)):
        for j in range(i+1, len(list1)):
            if list1[i] == list1[j]:
                return 'List has duplicates'
    return "List doesn't have duplicates"


print(has_duplicates([0, 1, 2, 5, 78, 4, 0]))
