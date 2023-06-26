'''Use the “Rectangle” class as implemented above for the following exercises:
1. Create a “Square” class as subclass of “Rectangle”.
2. Implement the “Square” constructor. The constructor should have only the x1, y1
coordinates and the size of the square. Notice which arguments you’ll have to use
when you invoke the “Rectangle” constructor when you use “super”.
3. Instantiate two objects of “Square”, invoke the area method and print the objects.
Make sure that all calculations are returning correct numbers and that the coordinates
of the squares are consistent with the size of the square used as argument.'''


class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def width(self):
        return abs(self.x2 - self.x1)

    def height(self):
        return abs(self.y2 - self.y1)

    def area(self):
        return abs(self.x2 - self.x1) * abs(self.y2 - self.y1)

    def circumference(self):
        return 2 * abs(self.x2 - self.x1) + 2 * abs(self.y2 - self.y1)

    def __str__(self):
        print(f'Координаты начального угла квадрата: ({self.x1}, {self.y1})')


class Square(Rectangle):
    def __init__(self, x1, y1, num):
        super().__init__(x1, y1, x1+num, y1+num)


a = Square(0, 0, 5)
b = Rectangle(0, 0, 5, 5)

a.__str__()
print(f'Длина ребра квадрата равна: {a.width()}')
print(f'Площадь квадрата равна: {a.area()}')
print(f'Периметр квадрата равен: {a.circumference()}')
