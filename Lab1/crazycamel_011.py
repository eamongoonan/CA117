import sys

def camelCase(string):
    return "".join([word.capitalize() + " " for word in string.split()]).strip()

if (__name__ == "__main__"):
    for line in sys.stdin:
        print(camelCase(line.strip()[::-1])[::-1])
