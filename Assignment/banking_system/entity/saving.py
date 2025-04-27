from entity.account import Account

class SavingsAccount(Account):
    def __init__(self, customer, balance=500.0, interest_rate=4.5):
        super().__init__(customer, acc_type="Savings", balance=balance)
        self.interest_rate = interest_rate

    def deposit(self, amount: float):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount: float):
        if self.balance - amount >= 500:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance. Minimum ₹500 must be maintained.")

    def calculate_interest(self):
        interest = (self.balance * self.interest_rate) / 100
        self.balance += interest
        print(f"Interest ₹{interest:.2f} added to balance.")
