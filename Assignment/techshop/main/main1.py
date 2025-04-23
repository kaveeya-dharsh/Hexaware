import sys
import os
# Make sure the root project folder is on the import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dao.customer_dao import CustomerDAO
from dao.product_dao import ProductServiceDao
from util.db_connect_util import DBConnUtil
from dao.techshop_impl import CustomerServiceImpl


def main():
    # Initialize the DAOs (which open the DB connection)
    customer_service = CustomerDAO()
    product_service = ProductServiceDao()
    customer_service1 = CustomerServiceImpl()

    while True:
        print("\n=== TechShop Management System ===")
        print("1. Customer Registration")
        print("2. Update Customer Information")
        print("3. View Customer Details")
        print("4. Product Catalog Management")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            print("\n=== Customer Registration ===")
            customer_id = input("Enter Customer ID: ")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            email = input("Enter Email: ")
            phone = input("Enter Phone: ")
            address = input("Enter Address: ")

            # Basic validation
            if not first_name or not email or not phone:
                print("First Name, Email, and Phone are required.")
                continue

            print(customer_service.create_customer(customer_id, first_name, last_name, email, phone, address))

        elif choice == "2":
            print("\n=== Update Customer Information ===")
            customer_id = input("Enter Customer ID to update: ")
            new_first_name = input("New First Name : ")
            new_last_name = input("New Last Name : ")
            new_email = input("New Email : ")
            new_phone = input("New Phone : ")
            new_address = input("New Address : ")

            print(customer_service1.update_customer_info(customer_id, first_name=new_first_name, last_name=new_last_name,
                                                        email=new_email, phone=new_phone, address=new_address))

        elif choice == "3":
            print("\n=== View Customer Details ===")
            customer_id = input("Enter Customer ID to view details: ")
            customer_details = customer_service1.get_customer_details(customer_id)
            print(customer_details)

        elif choice == "4":
            print("\n=== Product Catalog Management ===")
            print("1. Add Product")
            print("2. Update Product")
            print("3. View All Products")
            print("4. Delete Product")

            product_choice = input("Enter choice for Product Management: ").strip()

            if product_choice == "1":
                pid = int(input("Product ID: "))
                name = input("Name: ")
                desc = input("Description: ")
                price = float(input("Price: "))
                print(product_service.add_product(pid, name, desc, price))

            elif product_choice == "2":
                pid = int(input("Product ID to update: "))
                new_price = input("New price (leave blank to skip): ").strip()
                new_desc = input("New description (leave blank to skip): ").strip()
                price_val = float(new_price) if new_price else None
                desc_val = new_desc if new_desc else None
                print(product_service.update_product(pid, price=price_val, description=desc_val))

            elif product_choice == "3":
                products = product_service.view_all_products()
                if products:
                    print("\nID | Name | Description | Price")
                    for prod in products:
                        print(f"{prod[0]} | {prod[1]} | {prod[2]} | {prod[3]}")
                else:
                    print("No products found.")

            elif product_choice == "4":
                pid = int(input("Product ID to delete: "))
                print(product_service.delete_product(pid))

            else:
                print("Invalid choice for Product Management.")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    # Establish the connection once at the beginning
    connection = DBConnUtil.get_connection()

    # Run the main function
    main()
