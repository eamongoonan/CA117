from sys import argv
from math import pi

def drange(start, stop, step=1.0):
    nums = []
    i = start
    while (i <= stop):
        nums.append(i)
        i += step
    return nums

if __name__ == '__main__':
    h1 = 'Radius (m)'
    h4 = '-' * len(h1)
    h2 = 'Area (m^2)'
    h5 = '-' * len(h2)
    h3 = 'Volume (m^3)'
    h6 = '-' * len(h3)

    print('{:>s} {:>15s} {:>15s}'.format(h1, h2, h3))
    print('{:>s} {:>15s} {:>15s}'.format(h4, h5, h6))

    for i in drange(float(argv[1]), float(argv[3]), float(argv[2])):
        surf = 4 * pi * i ** 2
        vol = (4 / 3) * pi * i ** 3
        print('{:>10.1f} {:>15.2f} {:>15.2f}'.format(i, surf, vol))
