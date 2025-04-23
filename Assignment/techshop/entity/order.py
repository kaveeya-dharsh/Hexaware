class Order:
    def __init__(self, order_id, customer_id, order_date, total_amount):
        self.__order_id = order_id
        self.customer_id = customer_id  # Foreign key to Customer
        self.order_date = order_date
        self.total_amount = total_amount



  