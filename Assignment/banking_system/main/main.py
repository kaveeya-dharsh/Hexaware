import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dao.service_imp import BankRepositoryImpl
from entity.customer import Customer
from exception.customexception  import InsufficientFundException
from exception.customexception import InvalidAccountException
from util.dbconn import DBConnUtil

def main():
    system = BankRepositoryImpl()

    while True:
        print("\n--- HMBank System ---")
        print("1. Create Account")
        print("2. View All Accounts")
        print("3. Check Balance")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Transfer")
        print("7. View Account Details")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\n--- Create Account ---")
            fname = input("First Name: ")
            lname = input("Last Name: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            email = input("Email: ")
            phone = input("Phone Number: ")
            address = input("Address: ")
            acc_type = input("Account Type (Savings/Current/ZeroBalance): ")
            balance = float(input("Initial Deposit Amount: "))

            customer = Customer(None, fname, lname, dob, email, phone, address)
            system.create_account(customer, acc_type, balance)

        elif choice == '2':
            print("\n--- List of Accounts ---")
            accounts = system.list_accounts()
            for acc in accounts:
                print(acc)

        elif choice == '3':
            acc_no = int(input("Enter account number: "))
            try:
                balance = system.get_account_balance(acc_no)
                print(f"Available Balance: ₹{balance}")
            except InvalidAccountException as e:
                print("[Error]", e)

        elif choice == '4':
            acc_no = int(input("Enter account number: "))
            amount = float(input("Amount to deposit: "))
            try:
                new_balance = system.deposit(acc_no, amount)
                print(f"Deposited successfully. New Balance: ₹{new_balance}")
            except Exception as e:
                print("[Error]", e)

        elif choice == '5':
            acc_no = int(input("Enter account number: "))
            amount = float(input("Amount to withdraw: "))
            try:
                new_balance = system.withdraw(acc_no, amount)
                print(f"Withdrawn successfully. New Balance: ₹{new_balance}")
            except InsufficientFundException as e:
                print("[Error]", e)
            except Exception as e:
                print("[Error]", e)

        elif choice == '6':
            from_acc = int(input("From account: "))
            to_acc = int(input("To account: "))
            amount = float(input("Amount to transfer: "))
            try:
                system.transfer(from_acc, to_acc, amount)
            except Exception as e:
                print("[Error]", e)

        elif choice == '7':
            acc_no = int(input("Enter account number: "))
            try:
                details = system.get_account_details(acc_no)
                if details:
                    print(f"\nAccount ID: {details[0]}")
                    print(f"Type: {details[1]}")
                    print(f"Balance: ₹{details[2]}")
                    print(f"Customer: {details[3]} {details[4]} | Email: {details[5]}")
                else:
                    print("No account found.")
            except Exception as e:
                print("[Error]", e)

        elif choice == '8':
            print("Thank you for using HMBank!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    main()
connection=DBConnUtil.get_connection()
