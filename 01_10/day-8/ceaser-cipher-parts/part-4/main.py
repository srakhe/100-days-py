alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        # TODO-3: What happens if the user enters a number/symbol/space?
        position = alphabet.index(char)
        new_position = position + (shift_amount)
        end_text += alphabet[new_position % 26]

    print(f"Here's the {cipher_direction}d result: {end_text}")


# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo

print(logo)
# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
repeat = True
while repeat:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    cont = input('Do you want to continue? [yes/no]')
    if cont.lower() == 'no':
        repeat = False
