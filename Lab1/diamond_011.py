#!/usr/bin/evn python
import sys

def diamond(n):
    for i in range(1, n):
        line = i * "* "
        print("{:^{}}".format(line[0:-1], n * 2 - 1).rstrip())

    for i in range(n, 0, -1):
        line = i * "* "
        print("{:^{}}".format(line[0:-1], n * 2 - 1).rstrip())

if (__name__ == "__main__"):
    diamond(int(sys.argv[1]))
