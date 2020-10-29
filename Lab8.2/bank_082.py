class BankAccount:
    next_account_number = 16555232
    total_lodgements = 0
    interest_rate = 0.043

    def __init__(self, fname, sname, bal=0.0):
        self.forename = fname
        self.surname = sname
        self.balance = bal
        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1

    def lodge(self, ammount):
        BankAccount.total_lodgements += 1
        self.balance += ammount

    def apply_interest(self):
        self.balance += self.balance * BankAccount.interest_rate

    def __iadd__(self, amount):
        self.balance += amount
        BankAccount.total_lodgements += 1
        return self

    def __str__(self):
        return (
            "Name: {} {}\n"
            "Account number: {}\n"
            "Balance: {:.2f}"
        ).format(
            self.forename, self.surname,
            self.account_number,
            self.balance
        )
