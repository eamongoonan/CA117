from sys import stdin

if (__name__ == "__main__"):
    words = {word.strip().lower(): word.strip() for word in stdin}
    revs = [
        words[word] for word in sorted(words)
        if 4 < len(word) and (word[::-1] in words or word == word[::-1])
    ]

    print(revs)
