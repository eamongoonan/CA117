#!/usr/bin/evn python
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        sub_s, s = line.strip().lower().split()
        print(sub_s in s)
