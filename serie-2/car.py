class Car:
    def __init__(self,
                 brand: str,
                 model: int,
                 line: str,
                 price: float):
        self._brand = brand
        self._model = model
        self._line = line
        self._price = price

    def __str__(self):
        return f'{self._brand} - {self._line} - {self._model}'


