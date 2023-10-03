from car import Car


class Pickup(Car):
    def __init__(self,
                 brand: str,
                 model: int,
                 line: str,
                 price: float,
                 mileage: int):
        super().__init__(brand, model, line, price)
        self.__mileage = mileage

    def __str__(self):
        result = super().__str__()
        result += f' - {self.__mileage}'

        return result
