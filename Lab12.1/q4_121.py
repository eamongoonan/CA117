from sys import stdin

if (__name__ == "__main__"):
    for line in stdin:
        print(
            line[0] + "".join([
                (" " if ord("A") <= ord(c) <= ord("Z") else "") + c.lower()
                for c in line.strip()[1:]
            ])
        )
