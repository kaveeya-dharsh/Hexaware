import sys
import os

# Add the root folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from entity.customer import Customer
from entity.product import Products
from entity.order import Order
from entity.orderdetail import OrderDetail
from entity.inventory import Inventory
from dao.techshop_service import CustomerServiceProvider,ProductServiceProvider, OrderServiceProvider, OrderDetailServiceProvider, InventoryServiceProvider
from util.db_connect_util import DBConnUtil
from exception.customexception import InvalidCustomerIDException

class CustomerServiceImpl(CustomerServiceProvider):
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()  # Initialize the DAO to interact with the DB

    def calculate_total_orders(self, connection):
     cursor = connection.cursor()
     cursor.execute("SELECT COUNT(*) FROM Orders WHERE CustomerID=?", (self.customer_id,))  # Access the mangled name
     result = cursor.fetchone()
     return result[0] if result else 0

    def get_customer_details(self, customer_id):
     if customer_id:
        # Pass customer_id as a tuple to the execute method
        self.cursor.execute("SELECT FirstName, LastName, Email, Phone, Address FROM Customers WHERE CustomerID = ?", (customer_id,))
        result = self.cursor.fetchone()
        if result:
            # If a result is found, unpack it into the instance variables
            self.first_name, self.last_name, self.email, self.phone, self.address = result
            return result
        else:
            # Raise custom exception if no result is found
            raise InvalidCustomerIDException(customer_id=customer_id, message="Customer ID not found")

    


    def update_customer_info(self,customer_id,first_name=None, last_name=None, email=None, phone=None, address=None):
    # Update instance variables if new values are provided
     if customer_id:
        self.customer_id = customer_id
     if first_name:
        self.first_name = first_name
     if last_name:
        self.last_name = last_name
     if email:
        self.email = email
     if phone:
        self.phone = phone
     if address:
        self.address = address

    # Execute the update query
     self.cursor.execute(
        "UPDATE Customers SET FirstName=?, LastName=?, Email=?, Phone=?, Address=? WHERE CustomerID=?",
        (self.first_name, self.last_name, self.email, self.phone, self.address, self.customer_id)
     )
    
     print("Rows affected:", self.cursor.rowcount)  # For debugging
     self.conn.commit()
     return "Customer info updated successfully."



# -------------------- Product Service Implementation --------------------
class ProductServiceImpl(ProductServiceProvider):
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def get_product_details(self, product_id: int) -> str:
        self.cursor.execute("SELECT ProductName, Description, Price FROM Products WHERE ProductID = ?", product_id)
        result = self.cursor.fetchone()
        if result:
            return f"Product Name: {result[0]}, Description: {result[1]}, Price: ${result[2]:.2f}"
        else:
            return "Product not found."

    def update_product_info(self, product_id: int, price: float = None, description: str = None) -> str:
        update_fields = []
        params = []

        if price is not None:
            update_fields.append("Price = ?")
            params.append(price)
        if description:
            update_fields.append("Description = ?")
            params.append(description)

        if not update_fields:
            return "No update provided."

        params.append(product_id)
        query = f"UPDATE Products SET {', '.join(update_fields)} WHERE ProductID = ?"
        self.cursor.execute(query, params)
        self.conn.commit()
        return "Product info updated successfully."

    def is_product_in_stock(self, product_id: int) -> bool:
        self.cursor.execute("SELECT QuantityInStock FROM Inventory WHERE ProductID = ?", product_id)
        result = self.cursor.fetchone()
        return result[0] > 0 if result else False


# -------------------- Order Service Implementation --------------------
class OrderServiceImpl(OrderServiceProvider):
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def calculate_total_amount(self, order_id: int) -> float:
        self.cursor.execute("SELECT TotalAmount FROM Orders WHERE OrderID = ?", order_id)
        result = self.cursor.fetchone()
        return result[0] if result else 0.0

    def get_order_details(self, order_id: int) -> str:
        self.cursor.execute("""
            SELECT Orders.OrderDate, Products.ProductName, OrderDetails.Quantity, Products.Price
            FROM Orders
            JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
            JOIN Products ON OrderDetails.ProductID = Products.ProductID
            WHERE Orders.OrderID = ?
        """, order_id)
        rows = self.cursor.fetchall()
        if rows:
            order_details = "\n".join([f"Product: {row[1]}, Quantity: {row[2]}, Price: ${row[3]:.2f}" for row in rows])
            return f"Order Date: {rows[0][0]}\n{order_details}"
        else:
            return "Order not found."

    def update_order_status(self, order_id: int, status: str) -> str:
        self.cursor.execute("UPDATE Orders SET Status = ? WHERE OrderID = ?", status, order_id)
        self.conn.commit()
        return "Order status updated successfully."

    def cancel_order(self, order_id: int) -> str:
        self.cursor.execute("DELETE FROM Orders WHERE OrderID = ?", order_id)
        self.conn.commit()
        return "Order cancelled successfully."


# -------------------- Order Detail Service Implementation --------------------
class OrderDetailServiceImpl(OrderDetailServiceProvider):
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def calculate_subtotal(self, order_detail_id: int) -> float:
        self.cursor.execute("""
            SELECT OrderDetails.Quantity, Products.Price
            FROM OrderDetails
            JOIN Products ON OrderDetails.ProductID = Products.ProductID
            WHERE OrderDetailID = ?
        """, order_detail_id)
        result = self.cursor.fetchone()
        return result[0] * result[1] if result else 0.0

    def get_order_detail_info(self, order_detail_id: int) -> str:
        self.cursor.execute("""
            SELECT OrderDetails.Quantity, Products.ProductName, Products.Price
            FROM OrderDetails
            JOIN Products ON OrderDetails.ProductID = Products.ProductID
            WHERE OrderDetailID = ?
        """, order_detail_id)
        result = self.cursor.fetchone()
        if result:
            return f"Product: {result[1]}, Quantity: {result[0]}, Price: ${result[2]:.2f}"
        else:
            return "Order detail not found."

    def update_quantity(self, order_detail_id: int, quantity: int) -> str:
        self.cursor.execute("UPDATE OrderDetails SET Quantity = ? WHERE OrderDetailID = ?", quantity, order_detail_id)
        self.conn.commit()
        return "Order detail quantity updated successfully."

    def add_discount(self, order_detail_id: int, discount_percent: float) -> str:
        self.cursor.execute("""
            SELECT OrderDetails.Quantity, Products.Price
            FROM OrderDetails
            JOIN Products ON OrderDetails.ProductID = Products.ProductID
            WHERE OrderDetailID = ?
        """, order_detail_id)
        result = self.cursor.fetchone()
        if result:
            original_total = result[0] * result[1]
            discount_amount = original_total * (discount_percent / 100)
            new_total = original_total - discount_amount
            # Update discount (for simplicity, this would usually be in a discount column, but we are not adding it here)
            return f"Discount applied: ${discount_amount:.2f}, New total: ${new_total:.2f}"
        return "Order detail not found."


# -------------------- Inventory Service Implementation --------------------
class InventoryServiceImpl(InventoryServiceProvider):
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def get_product(self, inventory_id: int):
        self.cursor.execute("""
            SELECT Products.ProductName, Inventory.QuantityInStock
            FROM Inventory
            JOIN Products ON Inventory.ProductID = Products.ProductID
            WHERE Inventory.InventoryID = ?
        """, inventory_id)
        result = self.cursor.fetchone()
        if result:
            return f"Product: {result[0]}, Quantity in Stock: {result[1]}"
        else:
            return "Product not found in inventory."

    def get_quantity_in_stock(self, inventory_id: int) -> int:
        self.cursor.execute("SELECT QuantityInStock FROM Inventory WHERE InventoryID = ?", inventory_id)
        result = self.cursor.fetchone()
        return result[0] if result else 0

    def add_to_inventory(self, inventory_id: int, quantity: int) -> str:
        self.cursor.execute("UPDATE Inventory SET QuantityInStock = QuantityInStock + ? WHERE InventoryID = ?", quantity, inventory_id)
        self.conn.commit()
        return "Inventory updated successfully."

    def remove_from_inventory(self, inventory_id: int, quantity: int) -> str:
        self.cursor.execute("UPDATE Inventory SET QuantityInStock = QuantityInStock - ? WHERE InventoryID = ?", quantity, inventory_id)
        self.conn.commit()
        return "Inventory updated successfully."

    def update_stock_quantity(self, inventory_id: int, new_quantity: int) -> str:
        self.cursor.execute("UPDATE Inventory SET QuantityInStock = ? WHERE InventoryID = ?", new_quantity, inventory_id)
        self.conn.commit()
        return "Inventory quantity updated successfully."

    def is_product_available(self, inventory_id: int, quantity_to_check: int) -> bool:
        self.cursor.execute("SELECT QuantityInStock FROM Inventory WHERE InventoryID = ?", inventory_id)
        result = self.cursor.fetchone()
        return result[0] >= quantity_to_check if result else False

    def get_inventory_value(self, inventory_id: int) -> float:
        self.cursor.execute("""
            SELECT Inventory.QuantityInStock, Products.Price
            FROM Inventory
            JOIN Products ON Inventory.ProductID = Products.ProductID
            WHERE Inventory.InventoryID = ?
        """, inventory_id)
        result = self.cursor.fetchone()
        return result[0] * result[1] if result else 0.0

    def list_low_stock_products(self, threshold: int) -> list:
        self.cursor.execute("""
            SELECT Products.ProductName, Inventory.QuantityInStock
            FROM Inventory
            JOIN Products ON Inventory.ProductID = Products.ProductID
            WHERE Inventory.QuantityInStock < ?
        """, threshold)
        rows = self.cursor.fetchall()
        return [row[0] for row in rows] if rows else []

    def list_out_of_stock_products(self) -> list:
        self.cursor.execute("""
            SELECT Products.ProductName
            FROM Inventory
            JOIN Products ON Inventory.ProductID = Products.ProductID
            WHERE Inventory.QuantityInStock = 0
        """)
        rows = self.cursor.fetchall()
        return [row[0] for row in rows] if rows else []

    def list_all_products(self) -> list:
        self.cursor.execute("""
            SELECT Products.ProductName, Inventory.QuantityInStock
            FROM Inventory
            JOIN Products ON Inventory.ProductID = Products.ProductID
        """)
        rows = self.cursor.fetchall()
        return [(row[0], row[1]) for row in rows] if rows else []
