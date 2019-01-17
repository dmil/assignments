# DHRUMIL AND ORI

# Read vegetables.csv into a variable called vegetables.
import csv
from pprint import pprint
import json

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = [dict(row) for row in reader] # Convert Ordered Dict to regular dict (python 3.6 or higher)


# Group vegetables by color as a variable vegetables_by_color.
vegetables_by_color = {}
for veggie in vegetables:
    color = veggie['color']
    if color in vegetables_by_color:
        vegetables_by_color[color].append(veggie)
    else:
        vegetables_by_color[color] = [veggie]

pprint(vegetables_by_color)

# Output vegetables_by_color into a json
# called vegetables_by_color.json.
with open('vegetables_by_color.json', 'w') as f:
    json.dump(vegetables_by_color, f)
