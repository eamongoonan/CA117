from sys import stdin
from collections import defaultdict

if (__name__ == "__main__"):
    table = defaultdict(lambda: 0)
    for line in stdin:
        name, grades = line.strip().split(":")
        table[name] = grades.split(",")

    valid = []
    invalid = []
    for k, v in table.items():
        if all(map(lambda a: a.isnumeric(), v)):
            valid.append(k)
        else:
            invalid.append(k)

    for k in sorted(valid, key=lambda k: sum(map(int, table[k])), reverse=True):
        print(k, ":", sum(map(int, table[k])))

    if (invalid):
        print("Skipped:")
        print("\n".join([k for k in invalid]))
