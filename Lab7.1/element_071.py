class Element:
    def __init__(self, num, name, sym, boil):
        self.number = num
        self.name = name
        self.symbol = sym
        self.boiling_point = boil

    def print_details(self):
        print("Number:", self.number)
        print("Name:", self.name)
        print("Symbol:", self.symbol)
        print("Boiling point:", self.boiling_point, "K")
