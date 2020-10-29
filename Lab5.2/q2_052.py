from sys import stdin

if (__name__ == "__main__"):
    for word in stdin:
        aeiou = [ch for ch in word.strip().lower() if ch in "aeiou"]
        if aeiou == list("aeiou"):
            print(word.strip())
