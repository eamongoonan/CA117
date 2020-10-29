#!/usr/bin/evn python
import sys

def contains(sub_chars, string):
    for char in sub_chars:
        if not(char in string):
            return False
        else:
            string = string.replace(char, "", 1)
    return True

if (__name__ == "__main__"):
    for line in sys.stdin:
        test, string = line.strip().lower().split()
        print(contains(test, string))
