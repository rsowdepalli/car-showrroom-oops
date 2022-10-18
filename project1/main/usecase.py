from typing import List
from Car import Car
from Showroom import Showroom
from User import User


user1: User = User('Ramesh')
user2: User = User('Suresh')

showroom1: Showroom =  Showroom('Delhi', 'Pride Showroom')
showroom2: Showroom =  Showroom('Hyderabad', 'Yomoto')

cars_for_showroom1: List[Car] = [
    Car(
        brand='BMW',
        model='A200',
        color='Black',
        horse_power=1500,
        price=10000
    ),
    Car(
        brand='Audi',
        model='A200',
        color='Black',
        horse_power=1500,
        price=15000
    ),
    Car(
        brand='Mercedes',
        model='A200',
        color='Black',
        horse_power=1500,
        price=20000
    )
]

cars_for_showroom2: List[Car] = [
    Car(
        brand='Lexus',
        model='A200',
        color='Red',
        horse_power=1500,
        price=40000
    ),
    Car(
        brand='Range Rover',
        model='A200',
        color='White',
        horse_power=1500,
        price=100000
    ),
    Car(
        brand='Rolls Royce',
        model='A200',
        color='Midnight Blud',
        horse_power=1500,
        price=150000
    )
]

for car in cars_for_showroom1:
    showroom1.add_car(car)

for car in cars_for_showroom2:
    showroom2.add_car(car)

print ('Showroom 1 has following cars')
print (showroom1.get_all_cars())

print ('Showroom 2 has following cars')
print (showroom2.get_all_cars())

print ('User 1 trying to buy car')
user1.buy('Rolls Royce A200', showroom1)
user1.buy('Rolls Royce A200', showroom2)

print ('User 2 is trying to buy Audi A200')
user2.buy('Audi A200', showroom1)
user2.buy('Audi A200', showroom2)
