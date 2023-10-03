import datetime

from doctor import Doctor
from patient import Patient

patients: list[Patient] = []
doctors: list[Doctor] = []


def add_doctor():
    print('Ingrese a un médico')
    firstname = input('Ingrese el nombre: ')
    lastname = input('Ingrese los apellidos: ')
    dpi = int(input('Ingrese el DPI'))
    day = int(input('Ingrese el día de nacimiento: '))
    month = int(input('Ingrese el mes de nacimiento: '))
    year = int(input('Ingrese el año de nacimiento: '))
    birthdate = datetime.date(year, month, day)
    phone = input('Ingrese el teléfono: ')
    email = input('Ingrese el correo electrónico: ')
    specialty = input('Ingrese la especialidad: ')
    college_id = int(input('Ingrese el colegiado: '))
    sallary = float(input('Ingrese el salario: '))

    doctor = Doctor(
        firstname,
        lastname,
        dpi,
        birthdate,
        phone,
        email,
        specialty,
        college_id,
        sallary
    )

    doctors.append(doctor)


def add_patient():
    print('Ingrese a un paciente')
    firstname = input('Ingrese el nombre: ')
    lastname = input('Ingrese los apellidos: ')
    dpi = int(input('Ingrese el DPI'))
    day = int(input('Ingrese el día de nacimiento: '))
    month = int(input('Ingrese el mes de nacimiento: '))
    year = int(input('Ingrese el año de nacimiento: '))
    birthdate = datetime.date(year, month, day)
    phone = input('Ingrese el teléfono: ')
    email = input('Ingrese el correo electrónico: ')
    weight = float(input('Ingrese el peso: '))
    height = float(input('Ingrese la altura: '))
    gender = input('Ingrese el género: ')
    trigliceridos = int(input('Ingrese los trigliceridos: '))
    presion_sistolica = int(input('Ingrese presión sistolica: '))
    presion_diastolica = int(input('Ingrese presión diastolica: '))

    patient = Patient(
        firstname,
        lastname,
        dpi,
        birthdate,
        phone,
        email,
        weight,
        height,
        gender,
        trigliceridos,
        presion_sistolica,
        presion_diastolica
    )

    patients.append(patient)


def show_health(patient: Patient):
    print('Datos del paciente:')
    print(patient.firstname, patient.lastname)
    print(patient.get_imc())
    print(patient.get_presion())
    print(patient.get_trigliceridos())


def main():
    while True:
        print('Menú')
        print('1- Ingreso de médicos')
        print('2- Ingreso de pacientes')
        print('3- Ver estado de paciente')
        print('4- Ver pacientes de un médico')
        print('5- Salir')
        option = int(input('Ingrese una opción: '))

        if option == 1:
            add_doctor()
        elif option == 2:
            add_patient()
        elif option == 3:
            dpi = int(input('Ingrese el DPI: '))
            for patient in patients:
                if patient.dpi == dpi:
                    show_health(patient)
                    break
        elif option == 4:
            dpi = int(input('Ingrese el DPI: '))
            for doctor in doctors:
                if doctor.dpi == dpi:
                    for patient in doctor.patients:
                        print(patient)
        elif option == 5:
            break
        else:
            continue

main()