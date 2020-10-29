from sys import argv
from calendar import weekday

if (__name__ == "__main__"):
    poem_lines = [
        "Monday's child is fair of face",
        "Tuesday's child is full of grace",
        "Wednesday's child is full of woe",
        "Thursday's child has far to go",
        "Friday's child is loving and giving",
        "Saturday's child works hard for a living",
        "Sunday's child is fair and wise and good in every way"
    ]
    day = weekday(int(argv[3]), int(argv[2]), int(argv[1]))
    print(
        "You were born on a " + poem_lines[day].split()[0][:-2] +
        " and " + poem_lines[day] + "."
    )
