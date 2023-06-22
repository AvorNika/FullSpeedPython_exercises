'''2. Create a function that receives a list as parameter and returns the maximum value
in the list. As you iterate over the list you may want to keep the maximum value
found so far in order to keep comparing it with the next elements of the list.'''


def max_num(list1):
    max_numb = list1[0]
    for elem in list1:
        if max_numb < elem:
            max_numb = elem
    return max_numb


print(max_num([-1, 56, 8, 45, -230, 5]))
