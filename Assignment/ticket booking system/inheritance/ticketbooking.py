from enum import Enum

class EventType(Enum):
    MOVIE = 'Movie'
    SPORTS = 'Sports'
    CONCERT = 'Concert'

class Event:
    def __init__(self, event_name="", event_date="", event_time="", venue_name="", total_seats=0, ticket_price=0.0, event_type=EventType.MOVIE):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue_name = venue_name
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.ticket_price = ticket_price
        self.event_type = event_type

    def display_event_details(self):
        print(f"Event: {self.event_name}, Date: {self.event_date}, Time: {self.event_time}, Venue: {self.venue_name}, Type: {self.event_type.value}, Available Seats: {self.available_seats}, Price: {self.ticket_price}")

class Movie(Event):
    def __init__(self, event_name="", event_date="", event_time="", venue_name="", total_seats=0, ticket_price=0.0, genre="", actor_name="", actress_name=""):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, ticket_price, EventType.MOVIE)
        self.genre = genre
        self.actor_name = actor_name
        self.actress_name = actress_name

    def display_event_details(self):
        super().display_event_details()
        print(f"Genre: {self.genre}, Actor: {self.actor_name}, Actress: {self.actress_name}")

class Concert(Event):
    def __init__(self, event_name="", event_date="", event_time="", venue_name="", total_seats=0, ticket_price=0.0, artist="", concert_type=""):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, ticket_price, EventType.CONCERT)
        self.artist = artist
        self.concert_type = concert_type

    def display_event_details(self):
        super().display_event_details()
        print(f"Artist: {self.artist}, Concert Type: {self.concert_type}")

class Sports(Event):
    def __init__(self, event_name="", event_date="", event_time="", venue_name="", total_seats=0, ticket_price=0.0, sport_name="", teams_name=""):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, ticket_price, EventType.SPORTS)
        self.sport_name = sport_name
        self.teams_name = teams_name

    def display_event_details(self):
        super().display_event_details()
        print(f"Sport: {self.sport_name}, Teams: {self.teams_name}")

class TicketBookingSystem:
    def create_event(self, event_type, **kwargs):
        if event_type == "Movie":
            return Movie(**kwargs)
        elif event_type == "Concert":
            return Concert(**kwargs)
        elif event_type == "Sports":
            return Sports(**kwargs)
        else:
            return Event(**kwargs)

    def display_event_details(self, event):
        event.display_event_details()

    def book_tickets(self, event, num_tickets):
        if event.available_seats >= num_tickets:
            event.available_seats -= num_tickets
            total_cost = num_tickets * event.ticket_price
            print(f"Booking successful. Total cost: {total_cost}")
        else:
            print("Not enough seats available.")

    def cancel_tickets(self, event, num_tickets):
        event.available_seats += num_tickets
        print(f"{num_tickets} tickets canceled. Updated available seats: {event.available_seats}")

    def main(self):
        # Sample test logic
        movie = self.create_event("Movie", event_name="Avengers", event_date="2025-05-01", event_time="18:00", venue_name="Cineplex", total_seats=100, ticket_price=250.0, genre="Action", actor_name="Robert Downey Jr.", actress_name="Scarlett Johansson")
        self.display_event_details(movie)
        self.book_tickets(movie, 3)
        self.display_event_details(movie)
        self.cancel_tickets(movie, 1)
        self.display_event_details(movie)

# To simulate
if __name__ == "__main__":
    tbs = TicketBookingSystem()
    tbs.main()
