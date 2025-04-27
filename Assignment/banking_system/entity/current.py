from entity.account import Account

class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 10000

    def __init__(self, customer, balance=0.0):
        super().__init__(customer, acc_type="Current", balance=balance)

    def deposit(self, amount: float):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount: float):
        if self.balance + CurrentAccount.OVERDRAFT_LIMIT >= amount:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Overdraft limit exceeded.")

    def calculate_interest(self):
        print("No interest applicable for current accounts.")
