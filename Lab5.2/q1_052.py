from sys import argv

if (__name__ == "__main__"):
    print(
        argv[1][-int(argv[2]) % len(argv[1]):] +
        argv[1][:-int(argv[2]) % len(argv[1])]
    )
