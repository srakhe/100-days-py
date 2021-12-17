import random
from game_data import data
from art import logo, vs


def compare(person1, person2):
    print(f'Compare A: {person1["name"]}, {person1["description"]}, from {person1["country"]}')
    print(vs)
    print(f'Against B: {person2["name"]}, {person2["description"]}, from {person2["country"]}')

    choice = input('Who has more followers on Instagram? (A/B)').lower()

    if choice == 'a' and (person1['follower_count'] > person2['follower_count']):
        return True
    elif choice == 'b' and (person1['follower_count'] < person2['follower_count']):
        return True
    else:
        return False


def play_game():
    print(logo)

    person2 = random.choice(data)
    win = True
    score = 0
    while win:
        print('Your current score: ', score)
        person1 = person2
        person2 = random.choice(data)
        while person1 == person2:
            person2 = random.choice(data)
        win = compare(person1, person2)
        if win:
            score += 1
        print('\n' * 10)
    print('Final Score: ', score)


cont = 'y'
while cont == 'y':
    play_game()
    cont = input('Go again? (y/n)').lower()
    print('\n' * 10)
