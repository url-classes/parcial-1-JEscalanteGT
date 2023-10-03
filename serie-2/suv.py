from car import Car


class Suv(Car):
    def __init__(self,
                 brand: str,
                 model: int,
                 line: str,
                 price: float,
                 is_crashed: bool):
        super().__init__(brand, model, line, price)
        self.__is_crashed = is_crashed

    def __str__(self):
        result = super().__str__()
        if self.__is_crashed:
            result += ' - Chocada'
        else:
            result += ' - No Chocada'

        return result
