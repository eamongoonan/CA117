import sys

def keyval(items):
    return (items[0], items[1:])

if (__name__ == "__main__"):
    with open(sys.argv[1]) as file:
        yellow_pages = dict(
            keyval(line.strip().split())
            for line in file
        )

    for line in sys.stdin:
        name = line.strip()
        print("Name:", name)
        if name in yellow_pages:
            print("Phone:", yellow_pages[name][0])
            print("Email:", yellow_pages[name][1])
        else:
            print("No such contact")
