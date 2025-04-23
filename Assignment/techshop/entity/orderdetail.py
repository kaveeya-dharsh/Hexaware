class OrderDetail:
    def __init__(self, order_detail_id, order_id, product_id, quantity):
        self.__order_detail_id = order_detail_id
        self.order_id = order_id  # Foreign key to Order
        self.product_id = product_id  # Foreign key to Product
        self.quantity = quantity