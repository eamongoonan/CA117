from sys import stdin

if (__name__ == "__main__"):
    for word in stdin:
        if (list("evil") == [ch for ch in word.lower() if ch in "evil"]):
            print(word.strip())
