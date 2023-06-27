'''1. Implement an iterator class to return the square of all numbers from “a” to “b”.'''


class Iterator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self):
        return self

    def __next__(self):
        if self.a < self.b:
            value = self.a ** 2
            self.a += 1
            return value
        else:
            raise StopIteration


for val in Iterator(1, 5):
    print(val)
