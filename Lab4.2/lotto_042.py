from random import randint
from random import shuffle
from sys import argv
from itertools import combinations

if (__name__ == "__main__"):
    l = []
    l = foo(3)
    print(l)
    l = foo(5)
    print(l)
    nums = list(map(int, argv[1:]))
    combos = shuffle(list(combinations([i for i in range(1, 48)], len(nums))))
    print(len(combos))