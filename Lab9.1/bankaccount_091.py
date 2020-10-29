class BankAccount:
    next_account_number = 16555232
    total_lodgements = 0
    interest_rate = 0.043

    def __init__(self, fname, sname, bal=0.0, account_type="General"):
        self.forename = fname
        self.surname = sname
        self.balance = bal
        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1
        self.account_type = account_type

    def lodge(self, ammount):
        BankAccount.total_lodgements += 1
        self.balance += ammount

    def withdraw(self, ammount):
        if self.balance < ammount:
            print("Insufficient funds available")
            return 0
        else:
            self.balance -= ammount
            return ammount

    def __str__(self):
        return (
            "Name: {} {}\n"
            "Account number: {}\n"
            "Account type: {}\n"
            "Balance: {:.2f}"
        ).format(
            self.forename, self.surname,
            self.account_number,
            self.account_type,
            self.balance
        )

class SavingsAccount(BankAccount):
    def __init__(self, fname, sname, bal):
        BankAccount.__init__(self, fname, sname, bal, "Savings")

    def apply_interest(self):
        self.balance *= 1.01

    def __str__(self):
        return (
            "Name: {} {}\n"
            "Account number: {}\n"
            "Account type: {}\n"
            "Balance: {:.2f}\n"
            "Interest rate: 0.01"
        ).format(
            self.forename, self.surname,
            self.account_number,
            self.account_type,
            self.balance
        )

class CurrentAccount(BankAccount):
    def __init__(self, fname, sname, bal):
        BankAccount.__init__(self, fname, sname, bal, "Current")

    def __str__(self):
        return (
            "Name: {} {}\n"
            "Account number: {}\n"
            "Account type: {}\n"
            "Balance: {:.2f}\n"
            "Overdraft: -1000.00"
        ).format(
            self.forename, self.surname,
            self.account_number,
            self.account_type,
            self.balance
        )

    def withdraw(self, ammount):
        if self.balance - ammount < -1000:
            print("Insufficient funds available")
            return 0
        else:
            self.balance -= ammount
            return ammount
