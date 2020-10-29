from sys import argv
from itertools import chain

if (__name__ == "__main__"):
    str = argv[1]
    odds = [str[i] for i in range(1, len(str), 2)]
    even = [str[i] for i in range(0, len(str), 2)]
    min_lis = odds if len(odds) < len(even) else even
    min_lis.append("")

    print("".join(list(chain.from_iterable(zip(odds, even)))))
