from abc import ABC, abstractmethod
from datetime import datetime

# -------------------- Customer Service Interface --------------------

class CustomerServiceProvider(ABC):

    @abstractmethod
    def calculate_total_orders(self, customer_id: int) -> int:
        pass

    @abstractmethod
    def get_customer_details(self, customer_id: int) -> str:
        pass

    @abstractmethod
    def update_customer_info(self, customer_id: int, email: str = None, phone: str = None, address: str = None) -> str:
        pass


# -------------------- Product Service Interface --------------------

class ProductServiceProvider(ABC):

    @abstractmethod
    def get_product_details(self, product_id: int) -> str:
        pass

    @abstractmethod
    def update_product_info(self, product_id: int, price: float = None, description: str = None) -> str:
        pass

    @abstractmethod
    def is_product_in_stock(self, product_id: int) -> bool:
        pass


# -------------------- Order Service Interface --------------------

class OrderServiceProvider(ABC):

    @abstractmethod
    def calculate_total_amount(self, order_id: int) -> float:
        pass

    @abstractmethod
    def get_order_details(self, order_id: int) -> str:
        pass

    @abstractmethod
    def update_order_status(self, order_id: int, status: str) -> str:
        pass

    @abstractmethod
    def cancel_order(self, order_id: int) -> str:
        pass


# -------------------- Order Detail Service Interface --------------------

class OrderDetailServiceProvider(ABC):

    @abstractmethod
    def calculate_subtotal(self, order_detail_id: int) -> float:
        pass

    @abstractmethod
    def get_order_detail_info(self, order_detail_id: int) -> str:
        pass

    @abstractmethod
    def update_quantity(self, order_detail_id: int, quantity: int) -> str:
        pass

    @abstractmethod
    def add_discount(self, order_detail_id: int, discount_percent: float) -> str:
        pass


# -------------------- Inventory Service Interface --------------------

class InventoryServiceProvider(ABC):

    @abstractmethod
    def get_product(self, inventory_id: int):
        pass

    @abstractmethod
    def get_quantity_in_stock(self, inventory_id: int) -> int:
        pass

    @abstractmethod
    def add_to_inventory(self, inventory_id: int, quantity: int) -> str:
        pass

    @abstractmethod
    def remove_from_inventory(self, inventory_id: int, quantity: int) -> str:
        pass

    @abstractmethod
    def update_stock_quantity(self, inventory_id: int, new_quantity: int) -> str:
        pass

    @abstractmethod
    def is_product_available(self, inventory_id: int, quantity_to_check: int) -> bool:
        pass

    @abstractmethod
    def get_inventory_value(self, inventory_id: int) -> float:
        pass

    @abstractmethod
    def list_low_stock_products(self, threshold: int) -> list:
        pass

    @abstractmethod
    def list_out_of_stock_products(self) -> list:
        pass

    @abstractmethod
    def list_all_products(self) -> list:
        pass

