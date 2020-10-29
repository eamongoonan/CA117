from sys import stdin

if (__name__ == "__main__"):
    for line in stdin:
        line = line.strip()
        if not line.isnumeric():
            print(line, "is not a number")
        else:
            print("Thank you for", line)
            break
