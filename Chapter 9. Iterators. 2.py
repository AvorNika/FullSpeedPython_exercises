'''2. Implement an iterator class to return all the even numbers from 1 to (n).
'''


class Iterator:

    def __init__(self, n):
        self.a = 1
        self.b = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.a < self.b:
            value = self.a
            self.a += 1
            if value % 2 == 0:
                return value

        else:
            raise StopIteration


for val in Iterator(10):
    if val is not None:
        print(val)
