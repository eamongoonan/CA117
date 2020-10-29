from math import sqrt

class Point:
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return vec2(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return vec2(
            self.x - other.x,
            self.y - other.y
        )

    def __iadd__(self, other):
        self = self + other
        return self

    def __isub__(self, other):
        self = self - other
        return self

    def neg(self, other):
        return vec2(-self.x, -self.y)

    def magnitude(self):
        return sqrt(
            self.x ** 2 +
            self.y ** 2
        )

    def distance(self, other):
        return sqrt(
            (other.x - self.x) ** 2 +
            (other.y - self.y) ** 2
        )

    def unit(self):
        d = self.dist(self)
        return vec2(x / d, y / d)

    def reflect(self):
        self.x = -self.x
        self.y = -self.y
