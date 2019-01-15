# Reads name.txt into a variable my_name
with open('name.txt') as f:
    my_name = f.read()

# construct  greeting
greeting = 'Hello my name is ' + my_name + '.'

# write that to a file
with open('hello.txt', 'w') as f:
    f.write(greeting)

