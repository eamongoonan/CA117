from sys import stdin

class Time:
    @classmethod
    def abstime(cls, hrs=0, mins=0):
        max_mins = 24 * 60
        return ((mins + hrs * 60) % max_mins + max_mins) % max_mins

    def __init__(self, hrs=0, mins=0):
        self.mins = Time.abstime(hrs, mins)

    def __add__(self, other):
        return Time(0, Time.abstime(0, self.mins + other.mins))

    def __str__(self):
        return "{:02d}:{:02d}".format(self.mins // 60, self.mins % 60)

if (__name__ == "__main__"):
    for line in stdin:
        line = line.strip().split()
        h, m = map(int, line[0].split(":"))
        print(Time(h, m) + (Time(0, -int(line[1]))))
