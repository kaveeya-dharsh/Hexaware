class Booking:
    def __init__(self, booking_id: int, event: str, num_tickets: int, customer_list: list):
        self.booking_id = booking_id
        self.event = event
        self.num_tickets = num_tickets
        self.customer_list = customer_list

    def calculate_booking_cost(self):
        return self.num_tickets * self.event.ticket_price

    def book_tickets(self):
        if self.event.book_tickets(self.num_tickets):
            print(f"Booking successful for {self.num_tickets} tickets.")
        else:
            print("Not enough available seats!")

    def cancel_booking(self):
        self.event.cancel_booking(self.num_tickets)
        print(f"Booking cancelled for {self.num_tickets} tickets.")
