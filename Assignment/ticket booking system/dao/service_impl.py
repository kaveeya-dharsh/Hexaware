import pyodbc
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dao.service import IBookingSystemRepository
from util.db_connect import DBConnUtil

class BookingSystemRepositoryImpl(IBookingSystemRepository):
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor() 

    def create_event(self, event_name, date, time, total_seats, ticket_price, event_type, venue):
        try:
            query = """
                INSERT INTO Event (event_name, event_date, event_time, total_seats, available_seats, ticket_price, event_type, venue_name)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
            self.cursor.execute(query, (event_name, date, time, total_seats, total_seats, ticket_price, event_type,venue.venue_name))
            self.conn.commit()  # Commit the transaction
            print("Event created successfully!")
        except Exception as e:
            self.conn.rollback()
            print(f"Error creating event: {str(e)}")

    def get_event_details(self):
        try:
            query = "SELECT * FROM Event"
            self.cursor.execute(query)
            events = self.cursor.fetchall()
            for event in events:
                print(f"Event: {event.event_name}, Date: {event.event_date}, Time: {event.event_time}, "
                      f"Available Seats: {event.available_seats}, Ticket Price: {event.ticket_price}")
            return events
        except Exception as e:
            print(f"Error fetching event details: {str(e)}")

    def get_available_no_of_tickets(self):
        try:
            query = "SELECT event_name, available_seats FROM Event"
            self.cursor.execute(query)
            available_tickets = self.cursor.fetchall()
            for row in available_tickets:
                print(f"Event: {row.event_name}, Available Seats: {row.available_seats}")
            return available_tickets
        except Exception as e:
            print(f"Error fetching available tickets: {str(e)}")

    def calculate_booking_cost(self, event_name, num_tickets):
        try:
            query = "SELECT ticket_price FROM Event WHERE event_name = ?"
            self.cursor.execute(query, (event_name,))
            ticket_price = self.cursor.fetchone()[0]  # Get the ticket price from the first column of the result
            total_cost = ticket_price * num_tickets
            print(f"Total booking cost for {num_tickets} tickets: {total_cost}")
            return total_cost
        except Exception as e:
            print(f"Error calculating booking cost: {str(e)}")

    def book_tickets(self, event_name, num_tickets, customers):
        try:
            # Check if there are enough available seats
            query = "SELECT available_seats FROM Event WHERE event_name = ?"
            self.cursor.execute(query, (event_name,))
            available_seats = self.cursor.fetchone()[0]
            
            if available_seats >= num_tickets:
                # Update available seats for the event
                query = "UPDATE Event SET available_seats = available_seats - ? WHERE event_name = ?"
                self.cursor.execute(query, (num_tickets, event_name))
                self.conn.commit()

                # Create a new booking
                query = "INSERT INTO Booking (event_id, num_tickets, customer_list) VALUES (?, ?, ?)"
                self.cursor.execute("SELECT event_id FROM Event WHERE event_name = ?", (event_name,))
                event_id = self.cursor.fetchone()[0]  # Get the event ID
                
                customer_list = ', '.join([customer.customer_name for customer in customers])
                self.cursor.execute(query, (event_id, num_tickets, customer_list))
                self.conn.commit()
                
                print(f"Booking successful for {num_tickets} tickets!")
            else:
                print("Not enough available seats.")
        except Exception as e:
            self.conn.rollback()
            print(f"Error booking tickets: {str(e)}")

    def cancel_booking(self, booking_id):
        try:
            query = "DELETE FROM Bookings WHERE booking_id = ?"
            self.cursor.execute(query, (booking_id,))
            self.conn.commit()
            print(f"Booking with ID {booking_id} canceled successfully.")
        except Exception as e:
            self.conn.rollback()
            print(f"Error canceling booking: {str(e)}")

    # Implementing the abstract method to get booking details
    def get_booking_details(self, booking_id):
        try:
            query = "SELECT * FROM Booking WHERE booking_id = ?"
            self.cursor.execute(query, (booking_id,))
            booking_details = self.cursor.fetchone()
            if booking_details:
                print(f"Booking ID: {booking_details[0]}, Event ID: {booking_details[1]}, "
                      f"Num Tickets: {booking_details[2]}, Customers: {booking_details[3]}")
            else:
                print("No booking found with the provided booking ID.")
            return booking_details
        except Exception as e:
            print(f"Error fetching booking details: {str(e)}")
