class Event:
    def __init__(self, event_name: str, event_date: str, event_time: str, total_seats: int, available_seats: int,
                 ticket_price: float, event_type: str, venue: str):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price
        self.event_type = event_type
        self.venue = venue

    def calculate_total_revenue(self):
        return (self.total_seats - self.available_seats) * self.ticket_price

    def get_booked_no_of_tickets(self):
        return self.total_seats - self.available_seats

    def book_tickets(self, num_tickets: int):
        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            return True
        return False

    def cancel_booking(self, num_tickets: int):
        self.available_seats += num_tickets

    def display_event_details(self):
        print(f"Event: {self.event_name}\nDate: {self.event_date}\nTime: {self.event_time}\n"
              f"Total Seats: {self.total_seats}\nAvailable Seats: {self.available_seats}\n"
              f"Ticket Price: {self.ticket_price}\nVenue: {self.venue.venue_name}")
