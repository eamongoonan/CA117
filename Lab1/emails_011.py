#!/usr/bin/evn python
import sys

def name(email):
    first, second = email.split("@")[0].split(".")
    first = "".join([i for i in first if not i.isdigit()])
    second = "".join([i for i in second if not i.isdigit()])
    return first.capitalize() + " " + second.capitalize()

if (__name__ == "__main__"):
    for line in sys.stdin:
        print(name(line.strip()))
