from entity.event import Event
class Movie(Event):
    def __init__(self, event_name: str, event_date: str, event_time: str, total_seats: int, available_seats: int,
                 ticket_price: float, venue: str):
        super().__init__(event_name, event_date, event_time, total_seats, available_seats, ticket_price, "Movie", venue)

class Concert(Event):
    def __init__(self, event_name: str, event_date: str, event_time: str, total_seats: int, available_seats: int,
                 ticket_price: float, venue: str):
        super().__init__(event_name, event_date, event_time, total_seats, available_seats, ticket_price, "Concert", venue)

class Sport(Event):
    def __init__(self, event_name: str, event_date: str, event_time: str, total_seats: int, available_seats: int,
                 ticket_price: float, venue: str):
        super().__init__(event_name, event_date, event_time, total_seats, available_seats, ticket_price, "Sport", venue)
