class Employee:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def wages(self):
        return 0

    def __str__(self):
        return "\n".join([
            "Name: " + self.name,
            "Number: " + str(self.number),
            "Wages: {:.2f}".format(self.wages())
        ])

class Manager(Employee):
    def __init__(self, name, number, salary):
        Employee.__init__(self, name, number)
        self.salary = salary

    def wages(self):
        return self.salary / 52

class AssemblyWorker(Employee):
    def __init__(self, name, number, rate, hours):
        Employee.__init__(self, name, number)
        self.rate = rate
        self.hours = hours

    def wages(self):
        return self.rate * self.hours
