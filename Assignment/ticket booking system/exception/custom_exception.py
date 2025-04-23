class DatabaseConnectionError(Exception):
    """Raised when a database connection error occurs."""
    def __init__(self, message="Unable to connect to the database"):
        self.message = message
        super().__init__(self.message)

class EventNotFoundException(Exception):
    def __init__(self, event_name, message="Event not listed in the menu"):
        self.event_name = event_name
        self.message = f"Event '{self.event_name}' not found. {message}"
        super().__init__(self.message)

class InvalidBookingIDException(Exception):
    def __init__(self, booking_id, message="Invalid booking ID entered"):
        self.booking_id = booking_id
        self.message = f"Booking ID '{self.booking_id}' is invalid. {message}"
        super().__init__(self.message)

