from math import sqrt
from sys import stdin

def roots(a, b, c):
    try:
        thrower = sqrt((b ** 2) - (4 * a * c)) / (2 * a)
    except:
        return None
    bee = (-b) / (2 * a)
    return (bee + thrower, bee - thrower)

if (__name__ == "__main__"):
    for line in stdin:
        r = roots(*list(map(int, line.strip().split())))
        if r is None:
            print("None")
        else:
            print("r1 =", str(r[0]) + ", r2 =", str(r[1]))
