import datetime


class Person:
    def __init__(self,
                 firstname: str,
                 lastname: str,
                 dpi: int,
                 birthdate: datetime.date,
                 phone: str,
                 email: str):
        self.firstname = firstname
        self.lastname = lastname
        self.dpi = dpi
        self.birthdate = birthdate
        self.phone = phone
        self.email = email

