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
            num_words[int(num)]
            for num in line.strip().split()
        )))
