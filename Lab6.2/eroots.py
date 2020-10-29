import sys
from math import sqrt

for line in sys.stdin:
   a, b, c = line.split()
   if int(b) ** 2 - 4 * int(a) * int(c) < 0:
      print("None")
   else:
      r1 = str(((-int(b) + sqrt(int(b) ** 2 - 4 * int(a) * int(c))) / (2 * int(a))))
      r2 = str(((-int(b) - sqrt(int(b) ** 2 - 4 * int(a) * int(c))) / (2 * int(a))))
      print("r1 =", r1 + ", r2 =", r2)
