class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if (amount <= self.balance):
            self.balance -= amount
            return amount
        else:
            print("Insufficient funds available")
            return 0

    def __str__(self):
        return "Your current balance is: {:.2f} euro".format(self.balance)
