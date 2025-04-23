from abc import ABC, abstractmethod
from entity.venue import Venue

class Event(ABC):
    def __init__(self, event_id=None, event_name="", event_date="", event_time="", venue=None,
                 total_seats=0, available_seats=0, ticket_price=0.0, event_type=""):
        self.event_id = event_id
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue = venue  # Venue object
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price
        self.event_type = event_type

    @abstractmethod
    def display_event_details(self):
        pass

    def calculate_total_revenue(self):
        return (self.total_seats - self.available_seats) * self.ticket_price

    def get_booked_no_of_tickets(self):
        return self.total_seats - self.available_seats

    def book_tickets(self, num_tickets):
        if self.available_seats >= num_tickets:
            self.available_seats -= num_tickets
            return True
        return False

    def cancel_booking(self, num_tickets):
        self.available_seats += num_tickets


