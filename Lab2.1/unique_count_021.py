from sys import stdin
from collections import defaultdict
from string import punctuation

if (__name__ == "__main__"):
    words = defaultdict()
    for line in stdin:
        line = "".join([
            ch for ch in line.strip().lower()
            if ch not in punctuation
        ])

        for key in line.split():
            words[key] = 1
    print(len(words))
