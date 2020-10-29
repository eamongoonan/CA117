class Weight:
    OUNCES_PER_POUND = 16

    def __init__(self, pounds=0, ounces=0):
        self.ounces = pounds * 16 + ounces

    @classmethod
    def from_ounces(cls, ounces):
        return Weight(0, ounces)

    def __ne__(self, other):
        return self.ounces != other.ounces

    def __eq__(self, other):
        return not self != other

    def __lt__(self, other):
        return self.ounces < other.ounces

    def __gt__(self, other):
        return other < self

    def __le__(self, other):
        return self.ounces <= other.ounces

    def __ge__(self, other):
        return self.ounces >= other.ounces

    def __add__(self, other):
        return Weight(0, self.ounces + other.ounces)

    def __iadd__(self, other):
        self.ounces += other.ounces
        return self

    def __mul__(self, factor):
        return Weight(0, self.ounces * factor)

    def __str__(self):
        return "{} pound(s) and {} ounce(s)".format(
            self.ounces // 16,
            self.ounces % 16
        )
