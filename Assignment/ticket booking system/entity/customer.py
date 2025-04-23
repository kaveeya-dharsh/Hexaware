class Customer:
    def __init__(self, customer_id=None, customer_name="", email="", phone_number=""):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.email = email
        self.phone_number = phone_number

    def display_customer_details(self):
        print(f"Customer ID: {self.customer_id}, Name: {self.customer_name}, Email: {self.email}, Phone: {self.phone_number}")
