NAMES_PATH = 'Input/Names/invited_names.txt'
LETTER_PATH = 'Input/Letters/starting_letter.txt'
SAVE_PATH = 'Output/ReadyToSend/'

with open(NAMES_PATH, 'r') as file:
    content = file.readlines()
names_list = [name.strip() for name in content]

with open(LETTER_PATH, 'r') as file:
    letter_content = file.read()

for name in names_list:
    new_content = letter_content.replace('[name]', name)
    with open(SAVE_PATH + f'/letter_to_{name}.txt', 'w') as file:
        file.write(new_content)
