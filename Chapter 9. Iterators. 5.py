'''5. Implement an iterator class to return the fibonnaci sequence from the first element
up to (n). You can check the definition of the fibonnaci sequence in the function’s
chapter. These are the first numbers of the sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
55, 89, . . .'''


class Iterator:

    def __init__(self, n):
        self.a = 0
        self.b = n
        self.val_0 = 0
        self.val_1 = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a < self.b:
            self.val_1, self.val_0 = self.val_0 + self.val_1, self.val_1
            self.a += 1
            return self.val_0

        else:
            raise StopIteration


for val in Iterator(10):
    print(val)
