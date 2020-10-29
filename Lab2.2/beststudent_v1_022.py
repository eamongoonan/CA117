from sys import argv
from collections import defaultdict

if (__name__ == "__main__"):
    grade_map = defaultdict(lambda: [])
    with open(argv[1]) as file:
        for line in file:
            line = line.strip()
            grade_map[line[:2]].append(line[3:])

        print("Best student:", grade_map[max(grade_map)][0])
        print("Best mark:", max(grade_map))
