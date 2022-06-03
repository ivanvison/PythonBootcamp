import os
os.system('cls')

class Account():

    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account Owner: {self.owner}\nAccount Balance: ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} accepted. Keep 'em coming!")

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted.")
        else:
            print(f"Withdrawal of {amount} denied. Not enough funds")


account1 = Account('Benjamin',1000)
print(account1)
print(account1.owner)
print(account1.balance)
account1.deposit(500)
account1.withdraw(400)
account1.deposit(100)
account1.withdraw(2000)


