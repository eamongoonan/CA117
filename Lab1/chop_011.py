#!/usr/bin/evn python
import sys

def chop(string):
    if len(string) < 3:
        return ""
    else:
        return string[1:-1]

if (__name__ == "__main__"):
    for line in sys.stdin:
        chopped = chop(line.strip())
        if (chopped):
            print(chopped)
