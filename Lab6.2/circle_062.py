from sys import stdin
from math import sqrt

class vec2:
    x = 0
    y = 0

    def __init__(self, x, y):
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

    def dist(self, other):
        return sqrt(
            (other.x - self.x) ** 2 +
            (other.y - self.y) ** 2
        )

    def unit(self):
        d = self.dist(self)
        return vec2(x / d, y / d)
class circle:
    def __init__(self, centre, rad):
        self.centre = centre
        self.rad = rad
    centre = None
    rad = None

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    c1 = circle(vec2(x1, y1), r1)
    c2 = circle(vec2(x2, y2), r2)
    return 0.001 < (r1 + r2) - c1.centre.dist(c2.centre)
