class Triathlete:
    def __init__(self, name, id, times=None):
        self.name = name
        self.tid = id
        self.times = {} if times is None else times

    def add_time(self, key, time):
        self.times[key] = time

    def get_time(self, key):
        return self.times[key]

    def __str__(self):
        return (
            "Name: {}\n"
            "ID: {}\n"
            "Race time: {}"
        ).format(
            self.name,
            self.tid,
            sum(self.times.values()) if self.times else 0
        )
