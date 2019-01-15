# Reading a text file
with open('name.txt') as f:
    name = f.read()

# Writing a Text File
with open('hello.txt', 'w') as f:
    f.write('Hello, my name is ' + name + '.\n')
