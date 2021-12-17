import turtle
import pandas

IMAGE = 'blank_states_img.gif'
DATA = '50_states.csv'
correct_guesses = 0

screen = turtle.Screen()
screen.title('US STATES GUESSING GAME')
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pandas.read_csv(DATA)
state_names = data.state.to_list()
guessed = []


def draw_state_name(name, x, y):
    my_turtle = turtle.Turtle()
    my_turtle.speed('fastest')
    my_turtle.hideturtle()
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.write(name)


while not len(guessed) == 50:
    answer = screen.textinput(f'Guesses correct: {correct_guesses}/50', 'Guess a state:')
    if not answer:
        break
    answer = answer.title()
    if answer in state_names and answer not in guessed:
        guessed.append(answer)
        row = data[data.state == answer]
        draw_state_name(str(row.state.item()), int(row.x), int(row.y))
        correct_guesses += 1

print('Game Over, Guessed correctly: ', len(guessed))

if len(guessed) < 50:
    new_data = [state for state in state_names if state not in guessed]
    pandas.DataFrame(new_data).to_csv('missed_answers.csv')

turtle.mainloop()
