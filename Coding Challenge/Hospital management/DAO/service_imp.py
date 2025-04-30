import pyodbc
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from typing import List
from entity.model import Appointment
from DAO.service import HospitalService

from util.db_util import DBConnUtil
from exception.dbexception import DatabaseConnectionError
from exception.custom_exception import PatientNumberNotFoundException

class HospitalServiceimp(HospitalService):
    def __init__(self):
        self.connection = DBConnUtil.get_connection()
        self.cursor = self.connection.cursor()

    def getAppointmentById(self, appointmentId: int):
     try:
        self.cursor.execute("""
            SELECT 
                a.appointmentId,
                a.appointmentDate,
                a.description,
                p.patientId,
                p.firstName + ' ' + p.lastName AS patientName,
                d.doctorId,
                d.firstName + ' ' + d.lastName AS doctorName
            FROM Appointment a
            JOIN Patient p ON a.patientId = p.patientId
            JOIN Doctor d ON a.doctorId = d.doctorId
            WHERE a.appointmentId = ?
        """, appointmentId)

        row = self.cursor.fetchone()
        if row:
            return {
                "appointmentId": row.appointmentId,
                "appointmentDate": row.appointmentDate,
                "description": row.description,
                "patientId": row.patientId,
                "patientName": row.patientName,
                "doctorId": row.doctorId,
                "doctorName": row.doctorName
            }
        else:
            raise Exception(f"Appointment with ID {appointmentId} not found.")
     except Exception as e:
        print(f"Error in getting appointment by ID: {e}")
        return None

        
    def getAppointmentsForPatient(self, patientId: int) -> List[dict]:
     try:
        self.cursor.execute("""
             SELECT 
                a.appointmentId,
                a.appointmentDate,
                a.description,
                p.patientId,
                p.firstName + ' ' + p.lastName AS patientName,
                d.doctorId,
                d.firstName + ' ' + d.lastName AS doctorName
            FROM Appointment a
            JOIN Patient p ON a.patientId = p.patientId
            JOIN Doctor d ON a.doctorId = d.doctorId
            WHERE a.patientId = ?
        """, patientId)
        rows = self.cursor.fetchall()
        if not rows:
            raise PatientNumberNotFoundException(f"No appointments found for patient ID {patientId}")
        
        appointments = []
        for r in rows:
            appointments.append({
                'appointmentId': r.appointmentId,
                'patientId': r.patientId,
                'patientName': r.patientName,
                'doctorId': r.doctorId,
                'doctorName': r.doctorName,
                'appointmentDate': r.appointmentDate,
                'description': r.description
            })
        return appointments
    
     except PatientNumberNotFoundException as pne:
        print(f"Patient Error: {pne}")
        return []
     except Exception as e:
        print(f"Error fetching appointments for patient {patientId}: {e}")
        return []

         
    def getAppointmentsForDoctor(self, doctorId: int) -> List[dict]:
     try:
        self.cursor.execute("""
          SELECT 
                a.appointmentId,
                a.appointmentDate,
                a.description,
                p.patientId,
                p.firstName + ' ' + p.lastName AS patientName,
                d.doctorId,
                d.firstName + ' ' + d.lastName AS doctorName
            FROM Appointment a
            JOIN Patient p ON a.patientId = p.patientId
            JOIN Doctor d ON a.doctorId = d.doctorId
            WHERE a.doctorId = ?
        """, doctorId)
        rows = self.cursor.fetchall()
        if not rows:
            raise Exception(f"No appointments found for doctor ID {doctorId}")
        
        appointments = []
        for r in rows:
            appointments.append({
                'appointmentId': r.appointmentId,
                'patientId': r.patientId,
                'patientName': r.patientName,
                'doctorId': r.doctorId,
                'doctorName': r.doctorName,
                'appointmentDate': r.appointmentDate,
                'description': r.description
            })
        return appointments

     except Exception as e:
        print(f"Error fetching appointments for doctor {doctorId}: {e}")
        return []

        
    def scheduleAppointment(self, appointment: Appointment) -> bool:
        try:
            self.cursor.execute("""
                INSERT INTO Appointment (patientId, doctorId, appointmentDate, description)
                VALUES (?, ?, ?, ?)
            """, appointment.getPatientId(), appointment.getDoctorId(), appointment.getAppointmentDate(), appointment.getDescription())
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error scheduling appointment: {e}")
            return False
        
    def updateAppointment(self, appointment: Appointment) -> bool:
        try:
            self.cursor.execute("""
                UPDATE Appointment SET patientId = ?, doctorId = ?, appointmentDate = ?, description = ?
                WHERE appointmentId = ?
            """, appointment.getPatientId(), appointment.getDoctorId(), appointment.getAppointmentDate(),
                 appointment.getDescription(), appointment.getAppointmentId())
            self.connection.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            print(f"Error updating appointment: {e}")
            return False
        
    def cancelAppointment(self, appointmentId: int) -> bool:
        try:
            self.cursor.execute("DELETE FROM Appointment WHERE appointmentId = ?", appointmentId)
            self.connection.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            print(f"Error canceling appointment: {e}")
            return False