import re

class Customer:
    def __init__(self, customer_id=None, first_name="", last_name="", dob="", email="", phone_number="", address=""):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.phone_number = phone_number
        self.address = address

    def display_customer_info(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"DOB: {self.dob}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone_number}")
        print(f"Address: {self.address}")

    def is_valid_email(self):
        return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', self.email)

    def is_valid_phone(self):
        return re.match(r'^\d{10}$', self.phone_number)

