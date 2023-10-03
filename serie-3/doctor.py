import datetime

from patient import Patient
from person import Person


class Doctor(Person):
    def __init__(self,
                 firstname: str,
                 lastname: str,
                 dpi: int,
                 birthdate: datetime.date,
                 phone: str,
                 email: str,
                 specialty: str,
                 college_id: int,
                 sallary: float):
        super().__init__(firstname, lastname, dpi, birthdate, phone, email)
        self.specialty = specialty
        self.college_id = college_id
        self.__sallary = sallary
        self.patients: list[Patient] = []

    def add_patient(self, patient: Patient):
        self.patients.append(patient)
