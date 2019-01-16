import json
from pprint import pprint

with open('redcars.json', 'r') as f:
    red_cars = json.load(f)

# group by make
cars_by_make = {}
for car in red_cars:
    make = car['make']
    if make in cars_by_make:
        cars_by_make[make].append(car)
    else:
        cars_by_make[make] = [car]

with open('groupedredcars.json', 'w') as f:
    json.dump(cars_by_make, f)
