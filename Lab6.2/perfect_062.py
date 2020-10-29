from sys import stdin
from math import sqrt
from math import ceil

def sumFac(n):
    sum = 0
    for i in range(1, ceil(sqrt(n))):
        sum += (i + (n // i)) if n % i == 0 else 0
    return sum - n

def isPerfect(n):
    return n == sumFac(n)

if (__name__ == "__main__"):
    for line in stdin:
        print(isPerfect(int(line.strip())))
