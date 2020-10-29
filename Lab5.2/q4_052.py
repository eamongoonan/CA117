from sys import argv
from sys import stdin
from collections import defaultdict

if (__name__ == "__main__"):
    foods = defaultdict(lambda: 100)
    with open(argv[1]) as file:
        for line in file:
            f, c = line.strip().rsplit(maxsplit=1)
            foods[f] = int(c)

    cal_intake = {}
    for line in stdin:
        person, food_lis = line.strip().split(",", maxsplit=1)
        cal_intake[person] = sum([foods[f] for f in food_lis.split(",")])

    name_width = len(max(cal_intake.keys(), key=len))
    cal_width = len(str(max(cal_intake.values(), key=lambda n: len(str(n)))))
    for kv in sorted(cal_intake.items(), key=lambda kv: kv[1]):
        print("{:>{:}} : {:>{:}}".format(kv[0], name_width, kv[1], cal_width))
