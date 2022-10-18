
from Showroom import Showroom


class User:

    def __init__(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name

    def buy(self, car_name: int, showroom: Showroom) -> bool:
        price = showroom.buy_car(car_name)
        if price != 0:
            print (f'User {self._name} bought car {car_name} for price {price}')

        else:
            print (f'User {self._name} could not buy the car {car_name}')
        
