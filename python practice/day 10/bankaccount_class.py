class BankAccount:

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(F"{amount} deposited. new balance ={self.balance} ")

    def withdrawl(self, amount):
        if amount > self.balance:
            print("you dont have sufficient funds. ")
        elif amount == self.balance:
            self.balance = '0'
            print("transaction completed. ")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def display_balance(self):
        print(f"{self.account_holder}'s balance is: {self.balance}")


account1 = BankAccount("Vamsee")
account1.display_balance()          # Vamsee's balance is: 0

account1.deposit(1000)              # 1000 deposited. New balance: 1000
account1.withdrawl(300)             # 300 withdrawn. New balance: 700
account1.withdrawl(1000)            # Insufficient balance!
account1.display_balance()         # Vamsee's balance is: 700
