import json

# READING A JSON FILE
# with open('superheroes.json', 'r') as f:
#     data = json.load(f)

# print(data)

# WRITING A JSON FILE
rows = [
    {"name": "Rachel", "age": 34},
    {"name": "Monica", "age": 34},
    {"name": "Phoebe", "age": 37}
]

with open('friends.json', 'w') as f:
    json.dump(rows, f)
