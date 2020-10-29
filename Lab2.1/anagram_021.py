from sys import stdin

if (__name__ == "__main__"):
    for line in stdin:
        var, rav = line.strip().split()
        var = list(var)
        rav = list(rav)
        var.sort()
        rav.sort()
        
        print(var == rav)
