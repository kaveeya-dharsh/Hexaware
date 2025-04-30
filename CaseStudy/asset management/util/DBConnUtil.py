import pyodbc

def get_connection():
    try:
        conn_str = (
            'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=LAPTOP-4EPHICJP;'  
                'DATABASE=ASSET;'      
                'Trusted_Connection=yes;'
        )
        conn = pyodbc.connect(conn_str)
        return conn
    except pyodbc.Error as e:
        print("Database connection error:", e)
        return None
