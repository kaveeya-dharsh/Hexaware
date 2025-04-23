import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dao.service_impl import BookingSystemRepositoryImpl
from entity.customer import Customer
from util.db_connect import DBConnUtil

def main():
    system = BookingSystemRepositoryImpl()

    while True:
        print("\n--- Ticket Booking System ---")
        print("1. View Events")
        print("2. Book Tickets")
        print("3. Cancel Booking")
        print("4. View Booking Details")
        print("5. View Available Tickets")
        print("6. Create Events")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            events = system.get_event_details()
            for e in events:
                print(f"{e.event_id} | {e.event_name} | {e.event_date} | {e.event_time} | ₹{e.ticket_price} | Available: {e.available_seats}")

        elif choice == '2':
         try:
          event_id = int(input("Enter event ID: "))  # Changed from event_name to event_id
          num_tickets = int(input("Enter number of tickets: "))
          customer_list = []
          for i in range(num_tickets):
            print(f"\nCustomer {i + 1}:")
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            customer_list.append(Customer(None, name, email, phone))
            system.book_tickets(event_id, num_tickets, customer_list)  # Pass event_id instead
         except ValueError:
          print("[ERROR] Invalid input. Please enter numeric values where required.")

        elif choice == '3':
            booking_id = int(input("Enter booking ID to cancel: "))
            system.cancel_booking(booking_id)

        elif choice == '4':
            system.get_booking_details()
        
        elif choice == '5':
            system.get_available_no_of_tickets()

        elif choice == '6':
            event_name = input("Enter event name: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            time = input("Enter event time (HH:MM): ")
            total_seats = int(input("Enter total seats: "))
            ticket_price = float(input("Enter ticket price: "))
            event_type = input("Enter event type: ")
            venue_name = input("Enter venue name: ")
            address = input("Enter venue address: ")
            system.create_event(event_name, date, time, total_seats, ticket_price, event_type, venue_name,address)

        elif choice == '7':
            print("Exiting... Bye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
connection=DBConnUtil.get_connection()