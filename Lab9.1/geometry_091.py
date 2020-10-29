from math import sqrt
from functools import reduce

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other):
        return sqrt(
            (other.x - self.x) ** 2 +
            (other.y - self.y) ** 2
        )

    def magnitude(self):
        return sqrt(
            self.x ** 2 +
            self.y ** 2
        )

class Shape:
    def __init__(self, points):
        self.points = points

    def sides(self):
        return [
            p.distance(self.points[i + 1])
            for i, p in enumerate(self.points[:-1])
        ] + [self.points[0].distance(self.points[-1])]

    def perimeter(self):
        return sum(self.sides())

class Triangle(Shape):
    def area(self):
        s = sum(self.sides()) / 2
        return sqrt(
            s * reduce(
                lambda a, b: a * b,
                [s - side for side in self.sides()]
            )
        )

class Square(Shape):
    def area(self):
        return self.sides()[0] ** 2
