from abc import ABC, abstractmethod
from entity.customer import Customer

class Account(ABC):
    _last_acc_no = 1000

    def __init__(self, customer: Customer, acc_type="", balance=0.0):
        Account._last_acc_no += 1
        self.account_number = Account._last_acc_no
        self.account_type = acc_type
        self.balance = balance
        self.customer = customer

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: ₹{self.balance}")
        self.customer.display_customer_info()

    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass
