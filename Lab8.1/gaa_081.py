class Score:
    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def abs_score(self):
        return self.points + self.goals * 3

    def __gt__(self, other):
        return other.abs_score() < self.abs_score()

    def __ge__(self, other):
        return other.abs_score() <= self.abs_score()

    def __lt__(self, other):
        return self.abs_score() < other.abs_score()

    def __le__(self, other):
        return self.abs_score() <= other.abs_score()

    def __eq__(self, other):
        return self.abs_score() == other.abs_score()

    def __ne__(self, other):
        return self.abs_score() != other.abs_score()

    def __iadd__(self, other):
        self.goals += other.goals
        self.points += other.points
        return self

    def __add__(self, other):
        return Score(
            self.goals + other.goals,
            self.points + other.points
        )

    def __isub__(self, other):
        self.goals -= other.goals
        self.points -= other.points
        return self

    def __sub__(self, other):
        return Score(
            self.goals - other.goals,
            self.points - other.points
        )

    def __str__(self):
        return (
            "{} goal(s) and "
            "{} point(s)"
        ).format(self.goals, self.points)
