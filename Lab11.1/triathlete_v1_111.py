class Triathlete:
    def __init__(self, name, id):
        self.name = name
        self.tid = id

    def __str__(self):
        return (
            "Name: {}\n"
            "ID: {}"
        ).format(
            self.name,
            self.tid
        )
