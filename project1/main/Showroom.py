from typing import List
from Car import Car

class Showroom:

    def __init__(self, location: str, name: str): 
        self._location = location
        self._name = name
        self._cars: List[Car] = []

    def add_car(self, car: Car) -> bool:
        try: 
            self._cars.append(car)
            return True
        except:
            return False

    def get_all_cars(self) -> List[str]:
        result = []

        for car in self._cars:
            result.append(car.get_summary())

        return '\n--\n'.join(result)

    def buy_car(self, car_name: str) -> int:
        
        for car in self._cars:
            if car.get_car_name() == car_name:
                print (f'Buy car {car.get_summary()}')
                
                return car.get_price()

        print('Sorry! Showroom does not have the car')

        return 0
