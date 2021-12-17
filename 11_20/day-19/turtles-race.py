from turtle import Turtle, Screen
import random

screen = Screen()

colours = ['red', 'yellow', 'green', 'blue', 'orange', 'purple']


def init_screen():
    screen.setup(height=500, width=600)
    options_string = '\n'
    for colour in colours:
        options_string += ('\n' + colour)
    return screen.textinput('Place your bets!', f'Which colour turtle do you think will win the race? {options_string}')


def init_race():
    for colour in colours:
        new_turtle = Turtle(shape='turtle')
        new_turtle.color(colour)
        new_turtle.penup()

    init_x = -200
    init_y = -210
    i = 0
    for a_turtle in screen.turtles():
        a_turtle.goto(init_x, init_y + i)
        i += 70


def race():
    while True:
        for a_turtle in screen.turtles():
            a_turtle.forward(random.randint(0, 10))
            if a_turtle.xcor() >= 200:
                return a_turtle.pencolor()


bet_colour = init_screen()
init_race()
win_colour = race()

if bet_colour == win_colour:
    print(f'Congratulations, Your {bet_colour} turtle has won!!')
else:
    print(f'Sorry you bet for the {bet_colour} turtle, but the winner was the {win_colour} turtle')

screen.exitonclick()
