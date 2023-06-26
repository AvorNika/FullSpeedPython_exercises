'''1. Implement a class named “Rectangle” to store the coordinates of a rectangle given
by (x1, y1) and (x2, y2).
2. Implement the class constructor with the parameters (x1, y1, x2, y2) and store them
in the class instances using the “self” keyword.
3. Implement the “width()” and “height()” methods which return, respectively, the
width and height of a rectangle. Create two objects, instances of “Rectangle” to
test the calculations.
4. Implement the method “area” to return the area of the rectangle (width*height).
5. Implement the method “circumference” to return the perimeter of the rectangle
(2*width + 2*height).
6. Do a print of one of the objects created to test the class. Implement the “__str__”
method such that when you print one of the objects it print the coordinates as (x1,
y1)(x2, y2).'''


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
        print(f'Координаты двух угловых точек прямоугольника: ({self.x1}, {self.y1}) ({self.x2}, {self.y2})')


a = Rectangle(1, 5, 10, 2)
b = Rectangle(0, 0, 5, 5)

a.__str__()
print(f'Ширина прямоугольника: {a.width()}, длина прямоугольника: {a.height()}')
print(f'Площадь прямоугольника равна: {a.area()}')
print(f'Периметр прямоугольника равен: {a.circumference()}')
