#!/usr/bin/evn python
import sys

def to_dec(num, base):
    total = 0
    power = 0
    for digit in num[::-1]:
        total += int(digit) * int(base) ** power
        power += 1
    return total

if (__name__ == "__main__"):
    for line in sys.stdin:
        num, base = line.strip().split()
        print(to_dec(num, base))
