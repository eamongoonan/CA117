from collections import defaultdict
from sys import stdin
from string import punctuation

if (__name__ == "__main__"):
    counts = defaultdict(lambda: 0)
    for line in stdin:
        for token in line.strip().lower().split():
            word = token.translate(str.maketrans(".?,", "   ")).strip()
            counts[word] += 1

    for key in sorted(counts):
        print(key, ":", counts[key])
