# Read vegetables.csv
import csv
import json

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# filter whitelist colors

green_veggies = []
whitelist = ['green']
for row in rows:
    if row['color'] in whitelist:
        green_veggies.append(row)

print(json.dumps(green_veggies, indent=2))
