from sys import argv
from collections import defaultdict

def main():
    grade_map = defaultdict(lambda: [])
    with open(argv[1]) as file:
        for line in file:
            line = line.strip()
            try:
                grade_map[int(line[:2])].append(line[3:])
            except:
                print("Invalid mark", line[:2], "encountered. Skipping.")

        print("Best student(s):", ", ".join(grade_map[max(grade_map)]))
        print("Best mark:", max(grade_map))

if (__name__ == "__main__"):
    main()
