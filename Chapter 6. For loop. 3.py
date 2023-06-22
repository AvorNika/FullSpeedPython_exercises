'''3. Modify the previous function such that it returns a list with the first element being
the maximum value and the second being the index of the maximum value in the
list. Besides keeping the maximum value found so far, you also need to keep the
position where it occurred.'''


def max_num(list1):
    max_numb = list1[0]
    max_index = 0
    for i in range(len(list1)):
        if max_numb < list1[i]:
            max_numb = list1[i]
            max_index = i
    return [max_numb, max_index]


print(max_num([-1, 56, 8, 45, -230, 5]))
