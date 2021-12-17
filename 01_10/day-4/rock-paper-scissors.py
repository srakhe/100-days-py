import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
user = int(input('What do you choose? Enter 0 for rock, 1 for paper and 2 for scissors!'))
ai = random.randint(0, 2)
print('You chose: ')
print(choices[user])
print('Computer chose:')
print(choices[ai])

if user == ai:
    print('Game drawn!')
else:
    if (user == 0 and ai == 1) or (user == 1 and ai == 2) or (user == 2 and ai == 0):
        print('You lose!')
    else:
        print('You win!')
