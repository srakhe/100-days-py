import re

with open('hi_full.txt', 'r') as file:
    data = file.read()

data = str(data)

reg = re.findall(r'\D+', data)
new_string = ''
for word in reg:
    if word and not word == ' ' and not word == '\n' and not word == '.':
        new_string += word

print(new_string)
with open('new_hi.txt', 'w') as file:
    file.write(new_string)
