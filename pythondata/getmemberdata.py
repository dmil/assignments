import json
from pprint import pprint
import csv

# Read superheroes.json
with open('superheroes.json', 'r') as f:
	squad = json.load(f)

# Write header to CSV file
with open('members.csv', 'w') as f:
	writer = csv.writer(f)
	header = ['name', 'age', 'secretIdentity', 'powers', 'squadName',
		'homeTown', 'formed', 'secretBase', 'active']
	writer.writerow(header)

	# Loop over members and write one row per member
	members = squad['members']
	for member in members:
		name = member['name']
		age = member['age']
		secretIdentity = member['secretIdentity']
		powers = member['powers']


		squadName = squad['squadName']
		homeTown = squad['homeTown']
		formed = squad['formed']
		secretBase = squad['secretBase']
		active = squad['active']

		writer.writerow([name, age, secretIdentity, powers, squadName,
			homeTown, formed, secretBase, active])