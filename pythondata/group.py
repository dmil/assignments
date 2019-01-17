from pprint import pprint
import json

with open('redcars.json') as f:
	red_cars = json.load(f)

# group by make
red_cars_by_make = {}
for car in red_cars:
    make = car['make']
    if make in red_cars_by_make:
        red_cars_by_make[make].append(car)
    else:
        red_cars_by_make[make] = [car]

with open('red_cars_by_make.json','w') as f:
    json.dump(red_cars_by_make, f, indent=2)

