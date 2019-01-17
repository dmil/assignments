import csv

with open('testwrite.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = [dict(row) for row in reader] # Convert Ordered Dict to regular dict (python 3.6 or higher)

print(rows)
