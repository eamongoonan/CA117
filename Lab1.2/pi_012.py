from math import pi
from sys import argv

if (__name__ == "__main__"):
    print(("{:.{}f}").format(pi, argv[1]))
