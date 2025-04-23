class Venue:
    def __init__(self, venue_id=None, venue_name="", address=""):
        self.venue_id = venue_id
        self.venue_name = venue_name
        self.address = address

    def display_venue_details(self):
        print(f"Venue ID: {self.venue_id}, Name: {self.venue_name}, Address: {self.address}")
