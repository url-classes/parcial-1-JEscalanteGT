from car import Car


class Sedan(Car):
    def __init__(self,
                 brand: str,
                 model: int,
                 line: str,
                 price: float,
                 owner: str):
        super().__init__(brand, model, line, price)
        self.__owner = owner

    def __str__(self):
        result = super().__str__()
        result += f' - {self.__owner}'

        return result

