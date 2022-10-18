
class Car:

    def __init__(
        self, 
        brand: str, 
        model: str,
        color: str, 
        horse_power: int, 
        price: int
    ):
        self._brand = brand
        self._model = model
        self._color = color
        self._horse_power = horse_power
        self._price = price
        self._car_name = f'{self._brand} {self._model}'

    def get_car_name(self):
        return self._car_name

    def get_price(self):
        return self._price

    def get_summary(self) -> str:
        return f'''
        Car name - {self._brand} {self._model}
        Color - {self._color}
        Price - {self._price}
        '''

