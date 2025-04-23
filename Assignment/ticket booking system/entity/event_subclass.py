from entity.event import Event

class Movie(Event):
    def __init__(self, genre="", actor_name="", actress_name="", **kwargs):
        super().__init__(**kwargs)
        self.genre = genre
        self.actor_name = actor_name
        self.actress_name = actress_name
        self.event_type = "Movie"

    def display_event_details(self):
        print(f"[Movie] {self.event_name} | Genre: {self.genre} | Actor: {self.actor_name}, Actress: {self.actress_name}")



class Concert(Event):
    def __init__(self, artist="", concert_type="", **kwargs):
        super().__init__(**kwargs)
        self.artist = artist
        self.concert_type = concert_type
        self.event_type = "Concert"

    def display_event_details(self):
        print(f"[Concert] {self.event_name} | Artist: {self.artist} | Type: {self.concert_type}")



class Sport(Event):
    def __init__(self, sport_name="", teams_name="", **kwargs):
        super().__init__(**kwargs)
        self.sport_name = sport_name
        self.teams_name = teams_name
        self.event_type = "Sport"

    def display_event_details(self):
        print(f"[Sport] {self.event_name} | Sport: {self.sport_name} | Match: {self.teams_name}")

