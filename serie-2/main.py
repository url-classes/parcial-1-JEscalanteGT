from sedan import Sedan
from pickup import Pickup
from suv import Suv

sedans: list[Sedan] = [
    Sedan('Mazda', 2020, '3', 2000000, 'Jorge')
]
pickups: list[Pickup] = []
suvs: list[Suv] = []


def add_car():
    car_type = input('¿Qué tipo de carro desea ingresar? ')
    # Datos en común
    brand = input('Ingrese la marca: ')
    model = int(input('Ingrese el modelo: '))
    line = input('Ingrese la línea: ')
    price = float(input('Ingrese el precio: '))

    if car_type == 'sedan':
        # Datos específicos
        owner = input('Ingrese el dueño: ')
        sedan = Sedan(brand, model, line, price, owner)
        sedans.append(sedan)
    elif car_type == 'pickup':
        # Datos específicos
        mileage = int(input('Ingrese el kilometraje: '))
        pickup = Pickup(brand, model, line, price, mileage)
        pickups.append(pickup)
    else:
        # Datos específicos
        is_crashed = bool(input('¿Está chocado? '))
        suv = Suv(brand, model, line, price, is_crashed)
        suvs.append(suv)


def show_cars():
    car_type = input('¿Qué tipo de carros desea visualizar? ')
    if car_type == 'sedan':
        for sedan in sedans:
            print(sedan)
    elif car_type == 'pickup':
        for pickup in pickups:
            print(pickup)
    else:
        for suv in suvs:
            print(suv)


def main():
    while True:
        print('Menú')
        print('1- Añadir vehículo')
        print('2- Ver vehículos')
        print('3- Salir')
        option = int(input('Ingrese una opción: '))

        if option == 1:
            add_car()
        elif option == 2:
            show_cars()
        elif option == 3:
            break
        else:
            continue


main()
