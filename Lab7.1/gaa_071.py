class Score:
    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def abs_score(self):
        return self.points + self.goals * 3

    def greater_than(self, other):
        return other.abs_score() < self.abs_score()

    def less_than(self, other):
        return self.abs_score() < other.abs_score()

    def equal_to(self, other):
        return self.abs_score() == other.abs_score()
