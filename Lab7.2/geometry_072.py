from math import sqrt

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return Point(
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
        return Point(-self.x, -self.y)

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
        return Point(x / d, y / d)

    def __truediv__(self, scalar):
        return Point(self.x / scalar, self.y / scalar)

    def __str__(self):
        return "({:.1f}, {:.1f})".format(self.x, self.y)

class Segment:
    def __init__(self, p1=Point(), p2=Point()):
        self.p1 = p1
        self.p2 = p2

    def midpoint(self):
        return (self.p2 + self.p1) / 2

    def length(self):
        return self.p1.distance(self.p2)

class Circle:
    def __init__(self, point, rad=0):
        self.centre = point
        self.rad = rad

    def overlaps(self, other):
        return 0.001 < (self.rad + other.rad) - self.centre.distance(other.centre)
