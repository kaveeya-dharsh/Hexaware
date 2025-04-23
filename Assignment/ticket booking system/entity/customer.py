class Customer:
    def __init__(self, customer_name: str, email: str, phone_number: str):
        self.customer_name = customer_name
        self.email = email
        self.phone_number = phone_number

    def display_customer_details(self):
        print(f"Customer: {self.customer_name}\nEmail: {self.email}\nPhone: {self.phone_number}")
