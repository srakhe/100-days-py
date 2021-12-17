import random
import hangman_art
import hangman_words

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

done_letters = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    done_already = False
    print(done_letters)
    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess not in done_letters:
        done_letters.append(guess)
    else:
        done_already = True
    if not done_already:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
            print(f'{guess} is not in the word! Lives remaining: {lives}')
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win.")
    else:
        print('You already entered that letter, Try another!')
    # TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])
