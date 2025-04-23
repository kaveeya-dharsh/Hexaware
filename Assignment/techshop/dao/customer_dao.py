import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 
from util.db_connect_util import DBConnUtil
from  exception.customexception import CustomerIDAlreadyExistsException


class CustomerDAO:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def create_customer(self, customer_id, first_name, last_name, email, phone, address):
        """
        Inserts a new customer into the database. Checks for duplicate email and customer_id.
        """
        try:
            # Step 1: Check for duplicate customer_id
            self.cursor.execute("SELECT COUNT(*) FROM Customers WHERE CustomerID = ?", (customer_id,))
            if self.cursor.fetchone()[0] > 0:
                raise CustomerIDAlreadyExistsException(customer_id)

            # Step 2: Check for duplicate email
            self.cursor.execute("SELECT COUNT(*) FROM Customers WHERE Email = ?", (email,))
            if self.cursor.fetchone()[0] > 0:
                return " Email already exists. Please use a different email."

            # Step 3: Insert new customer
            self.cursor.execute("""
                INSERT INTO Customers (CustomerID, FirstName, LastName, Email, Phone, Address)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (customer_id, first_name, last_name, email, phone, address))
            self.conn.commit()
            return " Customer registered successfully."

        except CustomerIDAlreadyExistsException as e:
            return f"{e.message}"

        except Exception as e:
            print(f"[ERROR] Registration failed: {e}")
            return " Registration failed due to a system error."
