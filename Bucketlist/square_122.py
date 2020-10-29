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

def main():
    vert = [
        vec2(*map(int, line.strip().split()))
        for line in stdin
    ]

    if (0.0001 < vert[0].dist(vert[1]) - vert[1].dist(vert[2])):
        vert[1], vert[2] = vert[2], vert[1]

    d = vert[0].dist(vert[1])
    corrector = vert[0] - vert[1]
    corner = vert[2] + corrector if (vert[2] + corrector).dist(vert[0]) - d < 0.0001 else vert[2] - corrector

    print(corner.x, corner.y)

if (__name__ == "__main__"):
    main()
