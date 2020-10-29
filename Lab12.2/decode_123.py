from sys import stdin

def decode(line):
    chars = []
    i = 0
    while i < len(line):
        chars.append(line[i])
        i += 3 if line[i] in "aeiou" else 1
    return "".join(chars)

if (__name__ == "__main__"):
    for word in stdin:
        print(decode(word.strip()))
