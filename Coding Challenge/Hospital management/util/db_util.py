import pyodbc
import sys
import os

# Add the root folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from exception.dbexception import DatabaseConnectionError

class DBConnUtil:
    @staticmethod
    def get_connection():
        try:
            connection = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=LAPTOP-4EPHICJP;'  
                'DATABASE=HOSPITAL;'       
                'Trusted_Connection=yes;'   
            )
            print("Connection successful!")
            return connection
        except pyodbc.Error as e:
            raise DatabaseConnectionError(f"Error occurred while connecting to database: {e}")
        
# Call the get_connection method to establish the connection
connection = DBConnUtil.get_connection()
cursor = connection.cursor()

cursor.execute("SELECT DB_NAME();")
db_name = cursor.fetchone()[0]
print("Connected to database:", db_name)

