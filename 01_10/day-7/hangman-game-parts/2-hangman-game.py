import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# TODO-1: - Create an empty List called display.
guess = input("Guess a letter: ").lower()
display = []
for i in range(0, len(chosen_word)):
    display.append('_')

# TODO-2: - Loop through each position in the chosen_word
i = 0
for letter in chosen_word:
    if letter == guess:
        display[i] = letter
    i += 1

# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
print(display)
