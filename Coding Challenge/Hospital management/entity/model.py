class Patient:
    def __init__(self, patientId, firstName, lastName, dateOfBirth, gender, contactNumber, address):
        self.patientId = patientId
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.gender = gender
        self.contactNumber = contactNumber
        self.address = address

    def __str__(self):
        return f"Patient({self.patientId}, {self.firstName}, {self.lastName}, {self.dateOfBirth}, {self.gender}, {self.contactNumber}, {self.address})"

class Doctor:
   def __init__(self, doctorId, firstName, lastName, specialization, contactNumber):
        self.doctorId = doctorId
        self.firstName = firstName
        self.lastName = lastName
        self.specialization = specialization
        self.contactNumber = contactNumber

   def __str__(self):
        return f"Doctor({self.doctorId}, {self.firstName}, {self.lastName}, {self.specialization}, {self.contactNumber})" 

   

class Appointment:
    def __init__(self,  patientId, doctorId, appointmentDate, description,appointmentId="None"):
        self.appointmentId = appointmentId
        self.patientId = patientId
        self.doctorId = doctorId
        self.appointmentDate = appointmentDate
        self.description = description

    def __str__(self):
        return f"Appointment({self.appointmentId}, {self.patientId}, {self.doctorId}, {self.appointmentDate}, {self.description})"
    
    # Getter methods (optional if you want to access the attributes)
    def getAppointmentId(self):
        return self.appointmentId
    
    def getPatientId(self):
        return self.patientId
    
    def getDoctorId(self):
        return self.doctorId
    
    def getAppointmentDate(self):
        return self.appointmentDate
    
    def getDescription(self):
        return self.description
