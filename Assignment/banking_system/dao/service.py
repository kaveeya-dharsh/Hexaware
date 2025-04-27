from abc import ABC, abstractmethod

class ICustomerServiceProvider(ABC):

    @abstractmethod
    def get_account_balance(self, account_number: int) -> float:
        pass

    @abstractmethod
    def deposit(self, account_number: int, amount: float) -> float:
        pass

    @abstractmethod
    def withdraw(self, account_number: int, amount: float) -> float:
        pass

    @abstractmethod
    def transfer(self, from_account: int, to_account: int, amount: float):
        pass

    @abstractmethod
    def get_account_details(self, account_number: int):
        pass
from abc import ABC, abstractmethod
from entity.customer import Customer

class IBankServiceProvider(ABC):

    @abstractmethod
    def create_account(self, customer: Customer, acc_type: str, balance: float):
        pass

    @abstractmethod
    def list_accounts(self):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass

from abc import ABC, abstractmethod
from entity.customer import Customer

class IBankRepository(ABC):

    @abstractmethod
    def create_account(self, customer: Customer, acc_type: str, balance: float):
        pass

    @abstractmethod
    def list_accounts(self):
        pass

    @abstractmethod
    def get_account_balance(self, account_number: int) -> float:
        pass

    @abstractmethod
    def deposit(self, account_number: int, amount: float) -> float:
        pass

    @abstractmethod
    def withdraw(self, account_number: int, amount: float) -> float:
        pass

    @abstractmethod
    def transfer(self, from_account: int, to_account: int, amount: float):
        pass

    @abstractmethod
    def get_account_details(self, account_number: int):
        pass
