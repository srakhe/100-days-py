# Not the best way to do it (Have to make sure it is closed each time
file = open('myFile.txt')
content = file.read()
print(content)
file.close()

# Do this instead
with open('myFile.txt') as file:
    content = file.read()
    print(content)
# Auto-close

# When writing, file will be created if not found!
with open('myFile.txt', 'w') as file:
    content = 'This is not SAM'
    file.write(content)

with open('myFile.txt', 'a') as file:
    content = '\nAdditional content!'
    file.write(content)
