class Inventory:
    def __init__(self, inventory_id, product_id, quantity_in_stock, last_stock_update):
        self.__inventory_id = inventory_id
        self.product_id = product_id  # Foreign key to Product
        self.quantity_in_stock = quantity_in_stock
        self.last_stock_update = last_stock_update

