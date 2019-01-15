import csv
import json

# Read veggies.csv into a variable "vegetables"
with open('veggies.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)

# Save "vegetables"  as vegetables.json
with open('cookedveggies.json', 'w') as f:
    json.dump(vegetables, f, indent=2)
