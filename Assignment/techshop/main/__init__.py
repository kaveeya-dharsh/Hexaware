# Abstract Entity Classes

from abc import ABC, abstractmethod
from datetime import datetime

class AbstractCustomer(ABC):
    @abstractmethod
    def calculate_total_orders(self):
        pass

    @abstractmethod
    def get_customer_details(self):
        pass

    @abstractmethod
    def update_customer_info(self, email: str, phone: str, address: str):
        pass


class AbstractProduct(ABC):
    @abstractmethod
    def get_product_details(self):
        pass

    @abstractmethod
    def update_product_info(self, price: float, description: str):
        pass

    @abstractmethod
    def is_product_in_stock(self):
        pass


class AbstractOrder(ABC):
    @abstractmethod
    def calculate_total_amount(self):
        pass

    @abstractmethod
    def get_order_details(self):
        pass

    @abstractmethod
    def update_order_status(self, status: str):
        pass

    @abstractmethod
    def cancel_order(self):
        pass


class AbstractOrderDetail(ABC):
    @abstractmethod
    def calculate_subtotal(self):
        pass

    @abstractmethod
    def get_order_detail_info(self):
        pass

    @abstractmethod
    def update_quantity(self, quantity: int):
        pass

    @abstractmethod
    def add_discount(self, discount: float):
        pass


class AbstractInventory(ABC):
    @abstractmethod
    def get_product(self):
        pass

    @abstractmethod
    def get_quantity_in_stock(self):
        pass

    @abstractmethod
    def add_to_inventory(self, quantity: int):
        pass

    @abstractmethod
    def remove_from_inventory(self, quantity: int):
        pass

    @abstractmethod
    def update_stock_quantity(self, new_quantity: int):
        pass

    @abstractmethod
    def is_product_available(self, quantity_to_check: int):
        pass

    @abstractmethod
    def get_inventory_value(self):
        pass

    @abstractmethod
    def list_low_stock_products(self, threshold: int):
        pass

    @abstractmethod
    def list_out_of_stock_products(self):
        pass

    @abstractmethod
    def list_all_products(self):
        pass
