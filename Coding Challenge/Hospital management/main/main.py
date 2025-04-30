import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DAO.service_imp import HospitalServiceimp
from entity.model import Appointment
from exception.custom_exception import PatientNumberNotFoundException
from util.db_util import DBConnUtil

def main():
    # Create an instance of the HospitalService implementation
    hs = HospitalServiceimp()

    print("Welcome to the Hospital Management System")

    while True:
        # Display the main menu
        print("\n--- Main Menu ---")
        print("1. Get Appointment by ID")
        print("2. Get Appointments for Patient")
        print("3. Get Appointments for Doctor")
        print("4. Schedule Appointment")
        print("5. Update Appointment")
        print("6. Cancel Appointment")
        print("7. Exit")

        # Taking user input for the choice
        choice = input("Please enter a choice (1-7): ")

        # Handling user choices
        if choice == '1':
            # Get Appointment by ID
            try:
                appointmentId = int(input("Enter appointment ID: "))
                appointment = hs.getAppointmentById(appointmentId)
                if appointment:
                    print("\nAppointment Details:")
                    print(f"Appointment ID: {appointment['appointmentId']}")
                    print(f"Patient ID: {appointment['patientId']}")
                    print(f"Patient Name: {appointment['patientName']}")
                    print(f"Doctor ID: {appointment['doctorId']}")
                    print(f"Doctor Name: {appointment['doctorName']}")
                    print(f"Date: {appointment['appointmentDate']}")
                    print(f"Description: {appointment['description']}")
                else:
                     print("Appointment not found.")
            except ValueError:
                print("Invalid input! Please enter a valid appointment ID.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '2':
            # Get Appointments for Patient
            try:
                patientId = int(input("Enter patient ID: "))
                appointments = hs.getAppointmentsForPatient(patientId)
                if appointments:
                    print("\nAppointments for Patient ID:", patientId)
                    for appointment in appointments:
                        print("\nAppointment Details:")
                        print(f"Appointment ID: {appointment['appointmentId']}")
                        print(f"Patient ID: {appointment['patientId']}")
                        print(f"Patient Name: {appointment['patientName']}")
                        print(f"Doctor ID: {appointment['doctorId']}")
                        print(f"Doctor Name: {appointment['doctorName']}")
                        print(f"Date: {appointment['appointmentDate']}")
                        print(f"Description: {appointment['description']}")
                   
                else:
                    print(f"No appointments found for patient ID {patientId}.")
            except ValueError:
                print("Invalid input! Please enter a valid patient ID.")
            except PatientNumberNotFoundException as e:
                print(e)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '3':
            # Get Appointments for Doctor
            try:
                doctorId = int(input("Enter doctor ID: "))
                appointments = hs.getAppointmentsForDoctor(doctorId)
                if appointments:
                    for appointment in appointments:
                        print("\nAppointment Details:")
                        print(f"Appointment ID: {appointment['appointmentId']}")
                        print(f"Patient ID: {appointment['patientId']}")
                        print(f"Patient Name: {appointment['patientName']}")
                        print(f"Doctor ID: {appointment['doctorId']}")
                        print(f"Doctor Name: {appointment['doctorName']}")
                        print(f"Date: {appointment['appointmentDate']}")
                        print(f"Description: {appointment['description']}")
                else:
                    print(f"No appointments found for doctor ID {doctorId}.")
            except ValueError:
                print("Invalid input! Please enter a valid doctor ID.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '4':
            # Schedule Appointment
            try:
                patientId = int(input("Enter patient ID: "))
                doctorId = int(input("Enter doctor ID: "))
                appointmentDate = input("Enter appointment date (YYYY-MM-DD HH:MM:SS): ")
                description = input("Enter description: ")

                # Create an Appointment object
                appointment = Appointment(patientId=patientId, doctorId=doctorId, appointmentDate=appointmentDate, description=description)

                # Schedule the appointment
                success = hs.scheduleAppointment(appointment)
                if success:
                    print("Appointment scheduled successfully.")
                else:
                    print("Failed to schedule the appointment.")
            except ValueError:
                print("Invalid input! Please enter valid data.")

        elif choice == '5':
            # Update Appointment
            try:
                appointmentId = int(input("Enter appointment ID to update: "))
                patientId = int(input("Enter new patient ID: "))
                doctorId = int(input("Enter new doctor ID: "))
                appointmentDate = input("Enter new appointment date (YYYY-MM-DD HH:MM:SS): ")
                description = input("Enter new description: ")

                # Create an updated Appointment object
                updated_appointment = Appointment(appointmentId=appointmentId, patientId=patientId, doctorId=doctorId, appointmentDate=appointmentDate, description=description)

                # Update the appointment
                success = hs.updateAppointment(updated_appointment)
                if success:
                    print("Appointment updated successfully.")
                else:
                    print("Failed to update the appointment.")
            except ValueError:
                print("Invalid input! Please enter valid data.")

        elif choice == '6':
            # Cancel Appointment
            try:
                appointmentId = int(input("Enter appointment ID to cancel: "))
                success = hs.cancelAppointment(appointmentId)
                if success:
                    print("Appointment cancelled successfully.")
                else:
                    print("Failed to cancel the appointment.")
            except ValueError:
                print("Invalid input! Please enter a valid appointment ID.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '7':
            # Exit the program
            print("Exiting program.")
            break  # Exits the loop and ends the program

        else:
            # Invalid choice
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Run the main method
    main()
    conn=DBConnUtil.get_connection()
