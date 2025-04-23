import pyodbc
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dao.service import IBookingSystemRepository
from util.db_connect import DBConnUtil
from exception.custom_exception import EventNotFoundException
from exception.custom_exception import InvalidBookingIDException

class BookingSystemRepositoryImpl(IBookingSystemRepository):
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor() 

    def create_event(self, event_name, date, time, total_seats, ticket_price, event_type, venue_name,address):
     try:
        # Insert into Venue
        self.cursor.execute("INSERT INTO Venue (venue_name,address) VALUES (?,?)", (venue_name,address))
        self.cursor.execute("SELECT SCOPE_IDENTITY()")
        venue_id = self.cursor.fetchone()[0]

        # Insert into Event
        query = """
            INSERT INTO Event (event_name, event_date, event_time, total_seats, available_seats,
                               ticket_price, event_type, venue_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.cursor.execute(query, (event_name, date, time, total_seats, total_seats,
                                    ticket_price, event_type, venue_id))
        self.conn.commit()
        print("Event created successfully!")
     except Exception as e:
        self.conn.rollback()
        print(f"[ERROR] Could not create event: {str(e)}")


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


    def book_tickets(self, event_id, num_tickets, customer_list):
     try:
        cursor = self.conn.cursor()

        # Instead of querying by event_name, query directly by event_id
        cursor.execute("SELECT event_id, available_seats, ticket_price FROM Event WHERE event_id = ?", (event_id,))
        event = cursor.fetchone()

        if not event:
            raise EventNotFoundException(f"Event ID {event_id} not found.")

        event_id, available_seats, ticket_price = event

        if available_seats < num_tickets:
            print("Not enough seats available.")
            return

        cursor.execute("UPDATE Event SET available_seats = available_seats - ? WHERE event_id = ?", (num_tickets, event_id))

        customer_ids = []
        for customer in customer_list:
            cursor.execute(""" 
                INSERT INTO Customer (customer_name, email, phone_number)
                VALUES (?, ?, ?)
            """, (customer.customer_name, customer.email, customer.phone_number))
            cursor.execute("SELECT SCOPE_IDENTITY()")
            customer_id = cursor.fetchone()[0]
            customer_ids.append(customer_id)

        total_cost = ticket_price * num_tickets
        cursor.execute("""
            INSERT INTO Booking (customer_id, event_id, num_tickets, total_cost, booking_date)
            VALUES (?, ?, ?, ?, GETDATE())
        """, (customer_ids[0], event_id, num_tickets, total_cost))

        self.conn.commit()
        print("Booking successful.")

     except EventNotFoundException as enf:
        print(f"[ERROR] {enf}")
     except Exception as e:
        self.conn.rollback()
        print(f"[ERROR] Booking failed: {e}")

    def cancel_booking(self, booking_id):
     try:
        cursor = self.conn.cursor()

        cursor.execute("SELECT event_id, num_tickets FROM Booking WHERE booking_id = ?", (booking_id,))
        booking = cursor.fetchone()

        if not booking:
            raise InvalidBookingIDException(booking_id)

        event_id, num_tickets = booking

        cursor.execute("UPDATE Event SET available_seats = available_seats + ? WHERE event_id = ?", (num_tickets, event_id))
        cursor.execute("DELETE FROM Booking WHERE booking_id = ?", (booking_id,))

        self.conn.commit()
        print("Booking cancelled successfully.")

     except InvalidBookingIDException as ibe:
        print(f"[ERROR] {ibe}")
     except Exception as e:
        self.conn.rollback()
        print(f"[ERROR] Cancelling booking failed: {e}")


    def get_booking_details(self):
     try:
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT booking_id,event_id,num_tickets, total_cost, booking_date from booking
        """)
        rows = cursor.fetchall()

        if not rows:
            print("No bookings found.")
            return

        print(f"\n--- All Bookings ---")
        
        for row in rows:
          print(f"\nBooking ID: {row[0]}")
          print(f"Event ID: {row[1]}")
          print(f"Tickets: {row[2]}")
          print(f"Total Cost: ₹{row[3]}")
          print(f"Booking Date: {row[4]}")

     except Exception as e:
        print(f"[ERROR] Failed to fetch bookings: {e}")



