import random
from art import logo


def difficulty():
    diff = input('Choose a difficulty: easy or hard\n').lower()
    if diff == 'easy':
        return 10
    else:
        return 5


def check_range(guess_num, num_to_guess):
    if guess_num > num_to_guess:
        print('The number you entered is too high!, Guess again..')
    else:
        print('The number you entered is too low!, Guess again..')


def play_game():
    print(logo)
    print('Welcome to the number guessing game!')
    print('I\'m thinking of a number between 1 to 100!')
    number_to_guess = random.randint(1, 100)
    print('Okay got it!')

    chances = difficulty()

    guessed_number = 101
    while not guessed_number == number_to_guess and not chances == 0:
        print(f'You have {chances} chances remaining!')
        guessed_number = int(input('Enter your guess: '))
        if guessed_number == number_to_guess:
            print(f'You won! The number you guessed was right! {guessed_number}')
        else:
            check_range(guessed_number, number_to_guess)
        chances -= 1
        if chances == 0:
            print('Oops! You ran out of chances!')


play_again = True
while play_again:
    play_game()
    play_again = input('Play again? (y/n)').lower()
    play_again = True if play_again == 'y' else False
