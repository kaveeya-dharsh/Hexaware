class DatabaseConnectionError(Exception):
    """Raised when a database connection error occurs."""
    def __init__(self, message="Unable to connect to the database"):
        self.message = message
        super().__init__(self.message)

class DatabaseQueryError(Exception):
    """Raised when a query execution error occurs."""
    def __init__(self, message="Error occurred while executing the database query"):
        self.message = message
        super().__init__(self.message)

class CustomerNotFoundError(Exception):
    """Raised when a customer is not found in the database."""
    def __init__(self, message="Customer not found in the database"):
        self.message = message
        super().__init__(self.message)
