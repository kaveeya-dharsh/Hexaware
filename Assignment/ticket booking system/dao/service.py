from abc import ABC, abstractmethod

class IEventServiceProvider(ABC):
    @abstractmethod
    def create_event(self, event_name: str, date: str, time: str, total_seats: int, ticket_price: float, event_type: str, venue: str):
        pass

    @abstractmethod
    def display_event_details(self, event: str):
        pass

class IBookingSystemServiceProvider(ABC):
    @abstractmethod
    def book_tickets(self, event: str, num_tickets: int, customers: list):
        pass

    @abstractmethod
    def cancel_tickets(self, booking_id: int):
        pass


class IBookingSystemRepository(ABC):
    @abstractmethod
    def create_event(self, event_name: str, date: str, time: str, total_seats: int, ticket_price: float, event_type: str, venue: str):
        pass

    @abstractmethod
    def get_event_details(self):
        pass

    @abstractmethod
    def get_available_no_of_tickets(self):
        pass

    @abstractmethod
    def calculate_booking_cost(self, num_tickets: int):
        pass

    @abstractmethod
    def book_tickets(self, event_name: str, num_tickets: int, customers: list):
        pass

    @abstractmethod
    def cancel_booking(self, booking_id: int):
        pass

    @abstractmethod
    def get_booking_details(self, booking_id: int):
        pass

