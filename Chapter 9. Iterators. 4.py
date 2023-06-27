'''4. Implement an iterator class to return all numbers from (n) down to 0.'''


class Iterator:

    def __init__(self, n):
        self.a = 0
        self.b = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.a < self.b:
            value = self.b
            self.b -= 1
            return value

        else:
            raise StopIteration


for val in Iterator(10):
    print(val)
