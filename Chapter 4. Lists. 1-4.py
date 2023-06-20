'''Create a list named “l” with the following values ([1, 4, 9, 10, 23]).
1. Using list slicing get the sublists [4, 9] and [10, 23].
2. Append the value 90 to the end of the list “l”. Check the difference between list concatenation and the “append” method.
3. Calculate the average value of all values on the list. You can use the “sum” and “len” functions.
4. Remove the sublist [4, 9].'''
l = [1, 4, 9, 10, 23]
print(l[1:3])
print(l[-2:])

# l.append(90)
# print(l)
# l += [90]
# print(l)

print(sum(l) / len(l))

del l[1:3]
print(l)
