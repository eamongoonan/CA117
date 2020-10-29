import sys

if (__name__ == "__main__"):
    with open(sys.argv[1]) as file:
        yellow_pages = dict(
            line.strip().split()
            for line in file
        )

    for line in sys.stdin:
        name = line.strip()
        print("Name:", name)
        if name in yellow_pages:
            print("Phone:", yellow_pages[name])
        else:
            print("No such contact")
