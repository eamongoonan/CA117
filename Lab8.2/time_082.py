class Time:
    def __init__(self, h=0, m=0, s=0):
        self.hour = h
        self.minute = m
        self.second = s

        self.minute += self.second // 60
        self.second %= 60
        self.hour += self.minute // 60
        self.minute %= 60
        self.hour %= 24

    def __eq__(self, other):
        return self.time_to_seconds() == other.time_to_seconds()

    def __gt__(self, other):
        return self.time_to_seconds() > other.time_to_seconds()

    def __add__(self, other):
        return Time.seconds_to_time(
            self.time_to_seconds() +
            other.time_to_seconds()
        )

    def __iadd__(self, other):
        t = self + other
        self.hour = t.hour
        self.minute = t.minute
        self.second = t.second
        return self

    def __str__(self):
        return "The time is {:0>2}:{:0>2}:{:0>2}".format(
            self.hour,
            self.minute,
            self.second
        )

    def time_to_seconds(self):
        return (self.hour * 60 * 60) + (self.minute * 60) + self.second

    @classmethod
    def seconds_to_time(cls, s):
        t = Time()
        t.hour = s // (60 * 60)
        t.hour %= 24
        s %= 60 * 60
        t.minute = s // 60
        s %= 60
        t.second = s
        return t
