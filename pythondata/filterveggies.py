# DHRUMIL AND ORI
import csv
from pprint import pprint
import json

# Read vegetables.csv into a variable called vegetables
with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = [dict(row) for row in reader] # Convert Ordered Dict to regular dict (python 3.6 or higher)

# filter to only green vegtables using a whitelist

green_vegetables = []
whitelist = ['green']
for veggie in vegetables:
	# {'name': 'eggplant', 'color': 'purple'}
    if veggie['color'] in whitelist:
        green_vegetables.append(veggie)


# Print veggies to the terminal
pprint(green_vegetables)

# Write the veggies to greenveggies.json
with open('greenveggies.json', 'w') as f:
    json.dump(green_vegetables, f, indent=2)