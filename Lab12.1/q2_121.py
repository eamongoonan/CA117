from sys import stdin

if (__name__ == "__main__"):
    lines = [line.strip().split() for line in stdin]
    print([i for i in range(len(lines[0])) if lines[0][i] == lines[1][i]])
