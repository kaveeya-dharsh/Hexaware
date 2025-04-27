import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dao.service import IBankRepository
from util.dbconn import DBConnUtil
from datetime import datetime

class BankRepositoryImpl(IBankRepository):

    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def create_account(self, customer, acc_type, balance):
     cursor = self.conn.cursor()

    # Convert dob string to date format
     try:
        dob = datetime.strptime(customer.dob, '%Y-%m-%d').date()  # Ensure it's in YYYY-MM-DD format
     except ValueError:
        print("Error: Invalid Date Format. Please use 'YYYY-MM-DD'.")
        return  # Exit the function if the date format is invalid

     cursor.execute("""
        INSERT INTO Customers (first_name, last_name, dob, email, phone_number, address)
        VALUES (?, ?, ?, ?, ?, ?)
      """, (customer.first_name, customer.last_name, dob, customer.email, customer.phone_number, customer.address))

    # Get the customer_id from the inserted record
     cursor.execute("SELECT SCOPE_IDENTITY()")
     customer_id = cursor.fetchone()[0]

     cursor.execute("""
        INSERT INTO Accounts (customer_id, account_type, balance)
        VALUES (?, ?, ?)
      """, (customer_id, acc_type, balance))
    
     self.conn.commit()
     print(f"Account created for {customer.first_name} {customer.last_name}.")

    def list_accounts(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Accounts")
        return cursor.fetchall()

    def get_account_balance(self, account_number):
        cursor = self.conn.cursor()
        cursor.execute("SELECT balance FROM Accounts WHERE account_id = ?", (account_number,))
        result = cursor.fetchone()
        return result[0] if result else 0.0

    def deposit(self, account_number, amount):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE Accounts SET balance = balance + ? WHERE account_id = ?", (amount, account_number))
        self.conn.commit()
        return self.get_account_balance(account_number)

    def withdraw(self, account_number, amount):
        balance = self.get_account_balance(account_number)
        if balance >= amount:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE Accounts SET balance = balance - ? WHERE account_id = ?", (amount, account_number))
            self.conn.commit()
            return self.get_account_balance(account_number)
        else:
            raise Exception("Insufficient funds.")

    def transfer(self, from_account, to_account, amount):
        self.withdraw(from_account, amount)
        self.deposit(to_account, amount)
        print("Transfer successful.")

    def get_account_details(self, account_number):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT a.account_id, a.account_type, a.balance, c.first_name, c.last_name, c.email
            FROM Accounts a
            JOIN Customers c ON a.customer_id = c.customer_id
            WHERE a.account_id = ?
        """, (account_number,))
        return cursor.fetchone()
