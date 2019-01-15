import csv

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

# open a CSV file
with open('veggies.csv', 'w') as f:
	writer = csv.writer(f)
	# WRITE HEADER
	writer.writerow(['name', 'color', 'length'])
	# Loop through veggies
	for vegetable in vegetables:
		# Write each veggie to a CSV
		name = vegetable['name']
		color = vegetable['color']
		length_of_veggie = len(name)

		row = [name, color, length_of_veggie]

		writer.writerow(row)












