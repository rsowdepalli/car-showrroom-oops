# Implement a car showroom management for a city using 
# OOPS principles in python.

Functional Requirements:
- The city can have Multiple Showrooms   
- Each showroom can have multiple brand of cars
- There can be multiple cars for each brand
- A user can buy a car from showroom
- A user can get catalog / list of all cars present in the showroom


Possible Objects -> 
- Showroom
    - location: str
    - name: str
    - cars: List[Car]
    - get_all_cars() -> List[Car]
    - buy_car(<car_name>: str) -> int
    - add_car(car: Car) -> bool
- Car
    - Model: str
    - Brand name: str
    - Color: str
    - Horse Power: int
    - Price: int
    - get_summary() -> str
- User
    - Name: str
    - buy(<car_name>: str) -> int
    - owned_cars: List







