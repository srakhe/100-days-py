import random
from art import logo


def draw_card(cards):
    card = random.choice(cards)
    cards.remove(card)
    return card


def get_random_cards(cards):
    cards_chosen = []
    for i in range(0, 2):
        card = draw_card(cards)
        cards_chosen.append(card)
    return cards_chosen


def get_total(card_list):
    sum = 0
    for card in card_list:
        sum += card
    return sum


def has_blackjack(card_list):
    if 11 in card_list and 10 in card_list:
        return True
    else:
        return False


def play_game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    win_status = ''

    # Give 2 cards to each
    user_cards = get_random_cards(cards)
    print(f'User cards chosen are {user_cards}')
    ai_cards = get_random_cards(cards)
    print(f'Ai cards chosen are {ai_cards}')

    if get_total(user_cards) < 17:
        draw_another = 'n'
        while draw_another == 'y':
            user_cards.append(draw_card(cards))
            print(f'Card added to user\'s hand: {user_cards}')
            draw_another = input('Draw another card? (y/n)').lower()

    if get_total(user_cards) > 21:
        print('The user\'s total is > 21')
        win_status = 'Win'
    else:
        if get_total(user_cards) > get_total(ai_cards):
            print('User has greater total than ai')
            win_status = 'Win'
        elif get_total(user_cards) == get_total(ai_cards):
            print('User has same total as ai')
            win_status = 'Tie'
        else:
            print('User has less total than ai')
            win_status = 'Lose'

    return win_status


cont = 'y'
while cont == 'y':
    print('\n' * 10)
    print(logo)
    win_status = play_game()
    if win_status == 'Win':
        print('The user won!')
    elif win_status == 'Tie':
        print('The game was tied!')
    else:
        print('The user lost the game')
    cont = input('Play again? (y/n)').lower()
