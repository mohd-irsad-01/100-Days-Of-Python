class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Amount withrawn successfully")
        else:
            print("Insufficient balance or invalid amount")

    def get_balacne(self):
        return self.__balance
    
    def display_details(self):
        print("\nAccount Holder:", self.account_holder)
        print("Available Balance:", self.__balance)

account = BankAccount("Irsad", 5000)
account.display_details()

account.deposit(2000)
account.withdraw(1500)

print("\nFinal Balance:", account.get_balacne())
