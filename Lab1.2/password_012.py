import sys

def char_classes(string):
    classes = [0, 0, 0, 0]
    for char in string:
        classes[0] = 1 if (char.isdigit()) else classes[0]
        classes[1] = 1 if (char.isalpha() and char.islower()) else classes[1]
        classes[2] = 1 if (char.isalpha() and char.isupper()) else classes[2]
        classes[3] = 1 if not(char.isalpha() or char.isdigit()) else classes[3]
        if (sum(classes) == 4):
            break
    return sum(classes)

if (__name__ == "__main__"):
    for line in sys.stdin:
        print(char_classes(line.strip()))
