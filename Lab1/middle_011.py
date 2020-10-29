#!/usr/bin/evn python
import sys

def middle(string):
    length = len(string)
    if not(0 < length) or (length % 2 == 0):
        return "No middle character!"
    else:
        return string[(length - 1) // 2]

if (__name__ == "__main__"):
    for line in sys.stdin:
        print(middle(line.strip()))
