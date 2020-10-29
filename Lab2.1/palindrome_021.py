from sys import stdin
from string import punctuation

def palindrome(string):
    return string[::-1] == string

if (__name__ == "__main__"):
    for line in stdin:
        string = "".join([
            ch for ch in line.strip().lower()
            if ch not in punctuation and not ch.isspace()
        ])
        print(palindrome(string))
