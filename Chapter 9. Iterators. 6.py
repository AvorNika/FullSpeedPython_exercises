'''6. Implement an iterator class to return all consecutive pairs of numbers from 0 until
(n), such as (0, 1), (1, 2), (2, 3). . .'''


class Iterator:

    def __init__(self, n):
        self.a = 0
        self.b = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.a < self.b - 1:
            self.current = self.a
            self.next = self.current + 1
            self.a += 1
            return self.current, self.next

        else:
            raise StopIteration


for val in Iterator(10):
    print(val)
