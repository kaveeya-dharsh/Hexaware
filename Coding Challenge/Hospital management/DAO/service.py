from abc import ABC, abstractmethod
from typing import List
from entity.model import Appointment

class HospitalService(ABC):

    @abstractmethod
    def getAppointmentById(self, appointmentId: int) -> Appointment:
        pass

    @abstractmethod
    def getAppointmentsForPatient(self, patientId: int) -> List[Appointment]:
        pass

    @abstractmethod
    def getAppointmentsForDoctor(self, doctorId: int) -> List[Appointment]:
        pass

    @abstractmethod
    def scheduleAppointment(self, appointment: Appointment) -> bool:
        pass

    @abstractmethod
    def updateAppointment(self, appointment: Appointment) -> bool:
        pass

    @abstractmethod
    def cancelAppointment(self, appointmentId: int) -> bool:
        pass
