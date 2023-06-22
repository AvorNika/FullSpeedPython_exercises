'''6. Implement the function “is_sorted_dec” which is similar to the previous one but
all items must be sorted by decreasing order.'''


def is_sorted_dec(list1):
    for i in range(len(list1) - 1):
        if list1[i] < list1[i+1]:
            return False
    return True


print(is_sorted_dec([58, 45, 17, 5, 2]))
