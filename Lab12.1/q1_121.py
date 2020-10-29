from sys import argv

if (__name__ == "__main__"):
    offset = int(argv[2]) % len(argv[1])
    print(argv[1][offset:] + argv[1][:offset])
