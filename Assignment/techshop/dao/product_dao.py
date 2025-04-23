import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.db_connect_util import DBConnUtil
from exception.customexception import ProductIDAlreadyExistsException
from exception.customexception import ProductIDNotFoundException

class ProductServiceDao:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def add_product(self, productid, name, description, price):
     try:
        # Check if product ID already exists
        self.cursor.execute("SELECT COUNT(*) FROM Products WHERE Productid = ?", (productid,))
        if self.cursor.fetchone()[0] > 0:
            raise ProductIDAlreadyExistsException(productid)

        # Insert the new product
        self.cursor.execute("""
            INSERT INTO Products (Productid, productname, Description, Price)
            VALUES (?, ?, ?, ?)
        """, (productid, name, description, price))
        self.conn.commit()
        return " Product added successfully!"

     except ProductIDAlreadyExistsException as e:
        return f" {e.message}"

     except Exception as e:
        return f"Failed to add product: {e}"


    def update_product(self, product_id, price=None, description=None):
     try:
        # Check if product ID exists before updating
        self.cursor.execute("SELECT COUNT(*) FROM Products WHERE ProductID=?", (product_id,))
        if self.cursor.fetchone()[0] == 0:
            raise ProductIDNotFoundException(product_id)

        if price is not None:
            self.cursor.execute("UPDATE Products SET Price=? WHERE ProductID=?", (price, product_id))
        if description is not None:
            self.cursor.execute("UPDATE Products SET Description=? WHERE ProductID=?", (description, product_id))

        self.conn.commit()
        return "Product updated successfully!"
    
     except ProductIDNotFoundException as e:
        return str(e)
     except Exception as e:
        return f" Update failed due to an unexpected error: {e}"

    def view_all_products(self):
        self.cursor.execute("SELECT * FROM Products")
        return self.cursor.fetchall()

    def delete_product(self, product_id):
     try:
        # Check if product exists before attempting to delete
        self.cursor.execute("SELECT COUNT(*) FROM Products WHERE ProductID=?", (product_id,))
        if self.cursor.fetchone()[0] == 0:
            raise ProductIDNotFoundException(product_id)

        self.cursor.execute("DELETE FROM Products WHERE ProductID=?", (product_id,))
        self.conn.commit()
        return "✅ Product deleted successfully!"
    
     except ProductIDNotFoundException as e:
        return str(e)
     except Exception as e:
        return f" Deletion failed due to an unexpected error: {e}"

