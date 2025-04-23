import sys
import os

# Add the root folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from entity.event import Event
from entity.venue import Venue
from entity.customer import Customer
from dao.service_impl import BookingSystemRepositoryImpl

# Import custom exceptions
from exception.custom_exception import EventNotFoundException
from exception.custom_exception import InvalidBookingIDException
from util.db_connect import DBConnUtil

class MainModule:
    def __init__(self):
        self.repository = BookingSystemRepositoryImpl()

    def show_menu(self):
        print("\nWelcome to the Ticket Booking System")
        print("1. Create Event")
        print("2. Book Tickets")
        print("3. Cancel Booking")
        print("4. Get Available Tickets")
        print("5. Get Event Details")
        print("6. Exit")
        choice = input("Enter your choice: ")
        return choice

    def create_event(self):
        try:
            event_name = input("Enter event name: ")
            event_date = input("Enter event date (YYYY-MM-DD): ")
            event_time = input("Enter event time (HH:MM:SS): ")
            total_seats = int(input("Enter total seats: "))
            ticket_price = float(input("Enter ticket price: "))
            event_type = input("Enter event type (Movie/Sports/Concert): ")
            venue_name = input("Enter venue name: ")
            venue = Venue(venue_name=venue_name, address="Unknown Address")

            self.repository.create_event(event_name, event_date, event_time, total_seats, ticket_price, event_type, venue)

        except Exception as e:
            print(f"Error occurred while creating event: {e}")

    def book_tickets(self):
        try:
            event_name = input("Enter event name to book tickets: ")
            num_tickets = int(input("Enter number of tickets to book: "))
            customer_name = input("Enter your name: ")
            email = input("Enter your email: ")
            phone_number = input("Enter your phone number: ")
            customer = Customer(customer_name=customer_name, email=email, phone_number=phone_number)

            success = self.repository.book_tickets(event_name, num_tickets, [customer])
            if not success:
                raise EventNotFoundException(event_name)

        except EventNotFoundException as e:
            print(e)
        except Exception as e:
            print(f"Error occurred while booking tickets: {e}")

    def cancel_booking(self):
        try:
            booking_id = int(input("Enter booking ID to cancel: "))
            success = self.repository.cancel_booking(booking_id)
            if not success:
                raise InvalidBookingIDException(booking_id)

        except InvalidBookingIDException as e:
            print(e)
        except Exception as e:
            print(f"Error occurred while canceling booking: {e}")

    def get_available_tickets(self):
        try:
            self.repository.get_available_no_of_tickets()
        except Exception as e:
            print(f"Error occurred while fetching available tickets: {e}")

    def get_event_details(self):
        try:
            self.repository.get_event_details()
        except Exception as e:
            print(f"Error occurred while fetching event details: {e}")

    def run(self):
        try:
            while True:
                choice = self.show_menu()
                if choice == '1':
                    self.create_event()
                elif choice == '2':
                    self.book_tickets()
                elif choice == '3':
                    self.cancel_booking()
                elif choice == '4':
                    self.get_available_tickets()
                elif choice == '5':
                    self.get_event_details()
                elif choice == '6':
                    print("Exiting the system.")
                    break
                else:
                    print("Invalid choice, please try again.")
        except AttributeError:
            print("NullPointer-like Error: Attempted to access a method or attribute on a None object.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main_module = MainModule()
    main_module.run()
connection= DBConnUtil.get_connection()