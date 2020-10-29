from sys import stdin

def center(lines):
    maxw = len(max([line for line in lines], key=len))
    for line in lines:
        print(("{:^" + str(maxw) + "}").format(line))

if (__name__ == "__main__"):
    center([line.strip() for line in stdin])
