import csv
import json
from pprint import pprint

# Read vegetables.csv
with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = [dict(row) for row in reader] # Convert Ordered Dict to regular dict (python 3.6 or higher)

pprint(vegetables)

# Write vegetables.json
with open('vegetables.json', 'w') as f:
    json.dump(vegetables, f, indent=2)
