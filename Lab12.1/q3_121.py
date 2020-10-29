from sys import stdin

if (__name__ == "__main__"):
    for line in stdin:
        if [c for c in line.strip().lower() if c in "aeiou"] == list("aeiou"):
            print(line.strip())
