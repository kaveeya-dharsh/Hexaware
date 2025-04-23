import datetime

class Booking:
    booking_counter = 1  # static variable to auto-increment

    def __init__(self, customer=None, event=None, num_tickets=0):
        self.booking_id = Booking.booking_counter
        Booking.booking_counter += 1
        self.customer = customer
        self.event = event
        self.num_tickets = num_tickets
        self.total_cost = num_tickets * event.ticket_price if event else 0
        self.booking_date = datetime.datetime.now()

    def display_booking_details(self):
        print(f"Booking ID: {self.booking_id} | Date: {self.booking_date}")
        if self.customer:
            self.customer.display_customer_details()
        if self.event:
            self.event.display_event_details()
        print(f"Tickets: {self.num_tickets} | Total Cost: ₹{self.total_cost}")


