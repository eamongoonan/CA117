#!/usr/bin/evn python
import sys

def cap_ends(string):
    if (len(string) < 2):
        return ""
    else:
        return string[0].capitalize() + string[1:-1] + string[-1].capitalize()

if (__name__ == "__main__"):
    for line in sys.stdin:
        capped = cap_ends(line.strip())
        if capped:
            print(capped)
