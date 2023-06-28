'''4. Implement a generator that returns all numbers from (n) down to 0.'''


def nums(n):
    x = 0
    while x < n:
        yield n
        n -= 1


for num in nums(26):
    print(num)
