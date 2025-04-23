import sys
import os

# Add the root folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 

# Importing necessary classes
from dao.techshop_impl import CustomerServiceImpl
from util.db_connect_util import DBConnUtil

def main():
    # Create an instance of the CustomerServiceImpl class
    customer_service = CustomerServiceImpl()
    
    # Set customer ID and other required attributes
    customer_service.customer_id = 1 # Example: Set a specific Customer ID to work with
    customer_service.first_name = "John"
    customer_service.last_name = "Doe"
    customer_service.email = "john.doe@example.com"
    customer_service.phone = "123-456-7890"
    customer_service.address = "123 Main St"

    # Example: Get customer details
    customer_details = customer_service.get_customer_details()
    print("Customer Details:")
    print(customer_details)

    # Example: Calculate the total number of orders for a customer
    total_orders = customer_service.calculate_total_orders(customer_service.conn)
    print(f"Total Orders for Customer: {total_orders}")

    # Example: Update customer information
    result = customer_service.update_customer_info(email="new.email@example.com", phone="987-654-3210")
    print(result)

if __name__ == "__main__":
    # Establish the connection once at the beginning
    connection = DBConnUtil.get_connection()

    # Run the main function
    main()
