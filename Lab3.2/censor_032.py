import sys

def main():
    with open(sys.argv[1]) as file:
        black_list = {key.strip(): len(key.strip()) * "@" for key in file}
    content = [line.strip() for line in sys.stdin]
    for key in black_list:
        for i in range(len(content)):
            content[i] = content[i].replace(key, black_list[key])

    print("\n".join(content))

if (__name__ == "__main__"):
    main()
