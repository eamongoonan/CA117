from math import sqrt

class Point:
    x = 0
    y = 0

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

    def reflect(self):
        self.x = -self.x
        self.y = -self.y

    def midpoint(self, other):
        return Point(
            (self.x + other.x) / 2,
            (self.y + other.y) / 2
        )

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

class Circle:
    def __init__(self, centre=Point(), radius=0.0):
        self.centre = centre
        self.radius = radius

    def __str__(self):
        return (
            "Centre: {}\n"
            "Radius: {}"
        ).format(
            self.centre,
            self.radius
        )

    def __add__(self, other):
        return Circle(
            self.centre.midpoint(other.centre),
            self.radius + other.radius
        )
