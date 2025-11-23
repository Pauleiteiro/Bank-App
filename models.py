class BankAccount:
    def __init__(self, holder, initial_balance):
        self.holder = holder
        self.balance = initial_balance

    def deposit(self, value):
        self.balance += value
        print(f"Value of deposit is {value}€. Now you have {self.balance}")

    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
            print(f"Withdraw of {value}€. Now hou have {self.balance}")
        else:
            print("Denied operation, you don't have enough money.")

# This inherits from the BankAccount class
class SavingsAccount(BankAccount):
    def apply_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        print(f"Fees of {interest} applied. Your new balance is {self.balance}.")

    def withdraw(self, value):
        fee = 2
        fees_applied = value + fee
        super().withdraw(fees_applied)
        print(f"You withdraw {value}€. Your new balance is {self.balance}")

