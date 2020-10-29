class Employee:
    next_employee_number = 0

    def __init__(self, name, hourly_rate=9.25, hours_worked=0.0):
        self.name = name
        self.employee_number = Employee.next_employee_number
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        Employee.next_employee_number += 1

    def add_hours(self, hrs=0):
        self.hours_worked += hrs

    def __str__(self):
        return (
            "Name: {}\n"
            "ID: {}\n"
            "Hours: {:.2f}\n"
            "Rate: {:.2f}\n"
            "Wages: {:.2f}"
        ).format(
            self.name,
            self.employee_number,
            self.hours_worked,
            self.hourly_rate,
            self.hourly_rate * self.hours_worked
        )
