'''3. Create another generator to yield all the odd numbers from 1 to (n).'''


def odd_nums(n):
    x = 1
    while x < n:
        if x % 2 == 1:
            yield x
        x += 1


for num in odd_nums(26):
    print(num)
