from entity.account import Account

class ZeroBalanceAccount(Account):
    def __init__(self, customer, balance=0.0):
        super().__init__(customer, acc_type="ZeroBalance", balance=balance)

    def deposit(self, amount: float):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient funds.")

    def calculate_interest(self):
        print("No interest for zero balance accounts.")
