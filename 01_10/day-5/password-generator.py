# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

len_letters = len(letters)
len_symbols = len(symbols)
len_numbers = len(numbers)
# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ''
for i in range(0, nr_letters):
    password += letters[random.randint(0, len_letters - 1)]
for i in range(0, nr_numbers):
    password += symbols[random.randint(0, len_symbols - 1)]
for i in range(0, nr_symbols):
    password += numbers[random.randint(0, len_numbers - 1)]
print(f'Here is your password: {password}')

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = ''
password_len = nr_letters + nr_symbols + nr_numbers
for i in range(0, password_len):
    while not nr_letters == 0 or not nr_symbols == 0 or not nr_numbers == 0:
        choose_type = random.randint(0, 2)
        if choose_type == 0 and not nr_letters == 0:
            nr_letters -= 1
            password += letters[random.randint(0, len_letters - 1)]
        elif choose_type == 1 and not nr_symbols == 0:
            nr_symbols -= 1
            password += symbols[random.randint(0, len_symbols - 1)]
        elif choose_type == 2 and not nr_numbers == 0:
            nr_numbers -= 1
            password += numbers[random.randint(0, len_numbers - 1)]
print(f'Here is your password: {password}')

# CAN USE SHUFFLE FUNCTION!
