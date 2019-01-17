import csv

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

# Write the vegetable to a CSV file
with open('vegetables.csv', 'w') as f:
	writer = csv.writer(f)
	# Write Header
	writer.writerow(['name', 'color'])

	# Loop through each vegetable
	for x in vegetables:
		name = x['name']
		color = x['color']
		length_of_name = len(x['name'])
		# Write Data
		writer.writerow([name, color])

