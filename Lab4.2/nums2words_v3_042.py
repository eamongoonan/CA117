from sys import stdin
from sys import argv

if (__name__ == "__main__"):
    with open(argv[1]) as file:
        mappings = dict([
            line.strip().split()
            for line in file
        ])

    from sys import stdin

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

    for line in stdin:
        print(" ".join((
            mappings[num_words[int(num)]]
            for num in line.strip().split()
        )))
