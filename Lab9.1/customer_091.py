class Customer:
    def __init__(self, name, balance, *address, discount=0):
        self.name = name
        self.balance = balance
        self.address = address
        self.discount = discount

    def owes(self):
        return self.balance

    def __str__(self):
        return "\n".join([
            self.name,
            self.address[0],
            self.address[1],
            self.address[2],
            "Balance: {:.2f}".format(self.balance),
            "Discount: {}%".format(self.discount),
            "Amount due: {:.2f}".format(self.balance - (self.balance * (self.discount / 100)))
        ])

def ValuedCustomer(name, balance, *address):
    return Customer(name, balance, *address, discount=10)
