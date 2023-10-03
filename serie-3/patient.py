import datetime

from doctor import Doctor


class Patient(Doctor):
    def __init__(self,
                 firstname: str,
                 lastname: str,
                 dpi: int,
                 birthdate: datetime.date,
                 phone: str,
                 email: str,
                 weight: float,
                 height: float,
                 gender: str,
                 trigliceridos: int,
                 presion_sistolica: int,
                 presion_diastolica: int
                 ):
        super().__init__(firstname, lastname, dpi, birthdate, phone, email)
        self.weight = weight
        self.height = height
        self.gender = gender
        self.trigliceridos = trigliceridos
        self.presion_sistolica = presion_sistolica
        self.presion_diastolica = presion_diastolica

    def get_imc(self):
        result = self.weight / pow(self.height, 2)
        if result < 18.5:
            return 'Peso inferior'
        elif 18.5 < result < 24.9:
            return 'Peso normal'
        elif 24.9 < result < 29.9:
            return 'Peso superior'
        else:
            return 'Obesidad'

    def get_trigliceridos(self):
        if self.trigliceridos < 150:
            return 'Óptimo'
        elif 150 < self.trigliceridos < 199:
            return 'Límite'
        elif 200 < self.trigliceridos < 499:
            return 'Alto'
        else:
            return 'Muy alto'

    def get_presion(self):
        if self.presion_sistolica < 80 or self.presion_diastolica < 80:
            return 'Hipotensión'
        elif 80 < self.presion_sistolica < 120 and 60 < self.presion_diastolica < 80:
            return 'Normal'
        elif 120 < self.presion_sistolica < 129 and self.presion_diastolica < 80:
            return 'Elevada'
        elif 130 < self.presion_sistolica < 139 or 80 < self.presion_diastolica < 89:
            return 'Hipertensión nivel 1'
        elif self.presion_sistolica >= 140 or self.presion_diastolica >= 90:
            return 'Hipertensión nivel 2'
        else:
            return 'Crisis de hipertensión'
