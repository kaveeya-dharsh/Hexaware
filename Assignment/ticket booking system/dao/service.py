from abc import ABC, abstractmethod
from entity.venue import Venue

class IEventServiceProvider(ABC):
    @abstractmethod
    def create_event(self, event_name, date, time, total_seats, ticket_price, event_type, venue: Venue):
        pass

    @abstractmethod
    def get_event_details(self):
        pass

    @abstractmethod
    def get_available_no_of_tickets(self, event_name):
        pass
  

class IBookingSystemServiceProvider(ABC):
    @abstractmethod
    def calculate_booking_cost(self, num_tickets, ticket_price):
        pass

    @abstractmethod
    def book_tickets(self, event_name, num_tickets, customer_list):
        pass

    @abstractmethod
    def cancel_booking(self, booking_id):
        pass

    @abstractmethod
    def get_booking_details(self, booking_id):
        pass
    


class IBookingSystemRepository(ABC):

    @abstractmethod
    def create_event(self, event_name, date, time, total_seats, ticket_price, event_type, venue: Venue):
        pass

    @abstractmethod
    def get_event_details(self):
        pass

    @abstractmethod
    def get_available_no_of_tickets(self, event_name):
        pass

    @abstractmethod
    def book_tickets(self, event_name, num_tickets, customer_list):
        pass

    @abstractmethod
    def cancel_booking(self, booking_id):
        pass

    @abstractmethod
    def get_booking_details(self, booking_id):
        pass

