import json
from pprint import pprint

cars = [
    {"model": "Yaris", "make": "Toyota", "color": "red"},
    {"model": "Auris", "make": "Toyota", "color": "red"},
    {"model": "Camry", "make": "Toyota", "color": "green"},
    {"model": "Prius", "make": "Toyota", "color": "yellow"},
    {"model": "Civic", "make": "Honda", "color": "red"},
    {"model": "Model 3", "make": "Tesla", "color": "red"}
]

# filter to red cars
red_cars = []
whitelist = ['red']
for car in cars:
    if car['color'] in whitelist:
        red_cars.append(car)

pprint(red_cars)

with open('redcars.json', 'w') as f:
	json.dump(red_cars,f, indent=2)
