friends = [
    {"name": "Rachel", "age": 34},
    {"name": "Monica", "age": 34},
    {"name": "Phoebe", "age": 37}
]

# filter blacklist names

cool_people = []
blacklist = ['Monica']
for friend in friends:
    if friend['name'] not in blacklist:
        cool_people.append(friend)

print(cool_people)
