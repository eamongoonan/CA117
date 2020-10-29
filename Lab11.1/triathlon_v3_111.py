class Triathlete:
    def __init__(self, name, id, times=None):
        self.name = name
        self.tid = id
        self.times = {} if times is None else times

    def add_time(self, key, time):
        self.times[key] = time

    def get_time(self, key):
        return self.times[key]

    def times_total(self):
        return sum(self.times.values()) if self.times else 0

    def __eq__(self, other):
        return self.times_total() == other.times_total()

    def __lt__(self, other):
        return self.times_total() < other.times_total()

    def __gt__(self, other):
        return other < self

    def __str__(self):
        return (
            "Name: {}\n"
            "ID: {}\n"
            "Race time: {}"
        ).format(
            self.name,
            self.tid,
            self.times_total()
        )

class Triathlon:
    def __init__(self):
        self.mappings = {}

    def add(self, athlete):
        self.mappings[athlete.tid] = athlete

    def lookup(self, id):
        return None if id not in self.mappings else self.mappings[id]

    def remove(self, id):
        return self.mappings.pop(id, None)

    def best(self):
        return sorted(self.mappings.values(), key=lambda a: a.times_total())[0]

    def worst(self):
        return sorted(self.mappings.values(), key=lambda a: a.times_total())[-1]

    def __str__(self):
        return "\n".join(map(str, sorted(self.mappings.values(), key=lambda a: a.name)))
