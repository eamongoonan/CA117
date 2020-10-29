from sys import stdin

if (__name__ == "__main__"):
    print(sum([len(line.strip().split()) for line in stdin]))
