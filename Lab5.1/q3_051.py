from sys import stdin

if(__name__ == "__main__"):
    for word in stdin:
        word = [ch if ch.isupper() else "0" for ch in word]
        print(max("".join(word).strip("0").split("0"), key=len))
