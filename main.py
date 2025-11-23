from models import BankAccount, SavingsAccount

print("-----Initializing your Bank System-----")

conta_paulo = BankAccount("Paulo", 1600)
conta_paulo.withdraw(100)

conta_poupanca_paulo = SavingsAccount("Paulo", 5000)
conta_poupanca_paulo.withdraw(100)
conta_poupanca_paulo.withdraw(100)
