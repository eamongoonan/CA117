from sys import stdin

def doubles(word):
    count = 0
    for i, c in enumerate(word[1:-1]):
        if c in "aeiou" and word[i] == c and word[i + 2] != c:
            count += 1
    count += 1 if word[-1] in "aeiou" and word[-1] == word[-2] else 0
    return count

if (__name__ == "__main__"):
    print(max([line.strip() for line in stdin], key=doubles))
