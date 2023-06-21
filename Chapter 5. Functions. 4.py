'''4. Create a function named “average” that computes the average value of a list passed
as parameter to the function. Use the “sum” and “len” functions.'''
user_list = [int(i) for i in input().split()]


def average(list1):
    return sum(list1) / len(list1)


print(average(user_list))
