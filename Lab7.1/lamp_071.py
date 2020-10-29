class Lamp:
    def __init__(self, state=False):
        self.on = state

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def toggle(self):
        self.on = not self.on
