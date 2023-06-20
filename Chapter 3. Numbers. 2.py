'''Calculate the average of the following sequences of numbers:'''
a = ((2, 4), (4, 8, 9), (12, 14/6, 15))
for i in a:
    print(sum(i) / len(i), type(sum(i) / len(i)))
