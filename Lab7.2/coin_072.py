from random import randint

class Coin:
    states = ["Heads", "Tails"]
    def __init__(self):
        self.sideup = Coin.states[0]

    def getstate(self):
        return self.sideup

    def flip(self):
        self.sideup = Coin.states[randint(0, 1)]
    def __str__(self):
        return "Current state: " + self.sideup
