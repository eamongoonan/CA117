from sys import stdin
from collections import defaultdict

if (__name__ == "__main__"):
    num_words = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten"
    ]

    mappings = defaultdict(lambda: "unknown")
    mappings.update(dict(zip(
        [str(i) for i in range(len(num_words))],
        num_words
    )))

    for line in stdin:
        print(" ".join((
            mappings[token]
            for token in line.strip().split()
        )))
