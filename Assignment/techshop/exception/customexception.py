class InvalidDataException(Exception):
    def __init__(self, message="Invalid data provided"):
        self.message = message
        super().__init__(self.message)

class InsufficientStockException(Exception):
    def __init__(self, product_name, quantity_requested, quantity_available):
        self.product_name = product_name
        self.quantity_requested = quantity_requested
        self.quantity_available = quantity_available
        self.message = f"Not enough stock for {self.product_name}. Requested: {self.quantity_requested}, Available: {self.quantity_available}"
        super().__init__(self.message)

class IncompleteOrderException(Exception):
    def __init__(self, message="Order details are incomplete"):
        self.message = message
        super().__init__(self.message)

class PaymentFailedException(Exception):
    def __init__(self, order_id, message="Payment transaction failed"):
        self.order_id = order_id
        self.message = f"Payment for Order ID {self.order_id} failed. {message}"
        super().__init__(self.message)

class IOException(Exception):
    def __init__(self, message="Error occurred during file I/O operation"):
        self.message = message
        super().__init__(self.message)

class DatabaseAccessException(Exception):
    def __init__(self, message="Error occurred during database access"):
        self.message = message
        super().__init__(self.message)

class ConcurrencyException(Exception):
    def __init__(self, message="Concurrency issue detected. Please retry the operation"):
        self.message = message
        super().__init__(self.message)

class AuthenticationException(Exception):
    def __init__(self, message="Authentication failed. Please check your credentials"):
        self.message = message
        super().__init__(self.message)

class AuthorizationException(Exception):
    def __init__(self, message="You do not have permission to access this resource"):
        self.message = message
        super().__init__(self.message)

class CustomerIDAlreadyExistsException(Exception):
    def __init__(self, customer_id, message="Customer ID already exists"):
        self.customer_id = customer_id
        self.message = f"Customer ID {self.customer_id} already exists. {message}"
        super().__init__(self.message)

class InvalidCustomerIDException(Exception):
    def __init__(self, customer_id, message="Invalid or missing Customer ID"):
        self.customer_id = customer_id
        self.message = f"{message}: {customer_id}"
        super().__init__(self.message)

class ProductIDAlreadyExistsException(Exception):
    def __init__(self, product_id, message="Product ID already exists. Please use a different ID."):
        self.product_id = product_id
        self.message = f"Product ID {self.product_id} already exists. {message}"
        super().__init__(self.message)

class ProductIDNotFoundException(Exception):
    def __init__(self, product_id, message="Product ID not found in the database."):
        self.product_id = product_id
        self.message = f" Product ID '{self.product_id}' not found. {message}"
        super().__init__(self.message)

