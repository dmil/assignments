import csv

with open('testwrite.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

for row in rows:
    item = dict(row) # Convert Ordered Dict to regular dict (python 3.6 or higher)
    print(item)
