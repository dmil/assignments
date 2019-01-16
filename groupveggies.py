# DHRUMIL AND ORI
import csv
import json
from pprint import pprint

# Read vegetables.csv
with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)

# Group by color
veggies_by_color = {}
for v in vegetables:
    color = v['color']
    if color in veggies_by_color:
        veggies_by_color[color].append(v)
    else:
        veggies_by_color[color] = []
        veggies_by_color[color].append(v)

# Print to terminal
pprint(veggies_by_color)

# Output to JSON file
with open('veggies_by_color.json', 'w') as f:
    json.dump(veggies_by_color, f, indent=2)
