import json
# read superheroes.json
with open('superheroes.json', 'r') as f:
	superheroes = json.load(f)

# write a csv with rows per member
import csv

with open('superheroes.csv', 'w') as f:
	writer = csv.writer(f)

	# Write header
	headers = ['name', 'age', 'secretIdentity',
	'powers', 'squadName', 'homeTown', 'formed',
	'secretBase', 'active','firstpower']
	writer.writerow(headers)

	# Loop over the members
	members = superheroes['members']
	for member in members:
		# define variables
		name = member['name']
		age = member['age']
		secretIdentity = member['secretIdentity']
		powers = member['powers']

		squadName = superheroes['squadName']
		homeTown = superheroes['homeTown']
		formed = superheroes['formed']
		secretBase = superheroes['secretBase']
		active = superheroes['active']

		firstpower = member['powers'][0]

		# write data to csv file
		row = [
			name, age, secretIdentity, powers, squadName,homeTown,formed,secretBase,active,firstpower
		]
		writer.writerow(row)
