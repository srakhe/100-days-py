import time

from pong_field import PongField
from game_elements import GameElements
from score_board import ScoreBoard

MAX_X = 600
MAX_Y = 400
BALL_SPEED = 10
PLAYER_SPEED = 30

myField = PongField(MAX_X, MAX_Y)
p1 = GameElements('paddle', player_speed=PLAYER_SPEED)
p2 = GameElements('paddle', player_speed=PLAYER_SPEED)
ball = GameElements('ball')

score_p1 = ScoreBoard(side='l', max_y=MAX_Y)
score_p2 = ScoreBoard(side='r', max_y=MAX_Y)

myField.draw_border()
ball.init_game(player_number=0)
p1.init_game(player_number=1)
p2.init_game(player_number=2)

myField.bind_keys(p1, p2)

game_over = False
head_left = False
y_fact = 1
while not game_over:
    if head_left:
        ball.element.goto(ball.element.xcor() - BALL_SPEED, ball.element.ycor() + (BALL_SPEED * y_fact))
    else:
        ball.element.goto(ball.element.xcor() + BALL_SPEED, ball.element.ycor() + (BALL_SPEED * y_fact))
    if ball.element.xcor() < - MAX_X or ball.element.xcor() > MAX_X:
        game_over = True
    elif ball.element.ycor() < - (MAX_Y - 20):
        y_fact = 1
    elif ball.element.ycor() > (MAX_Y - 20):
        y_fact = -1
    elif ball.element.distance(p1.element) < 60 and ball.element.xcor() <= -(MAX_X - 80):
        score_p1.add_score()
        head_left = False
    elif ball.element.distance(p2.element) < 60 and ball.element.xcor() >= (MAX_X - 80):
        score_p2.add_score()
        head_left = True
    time.sleep(0.04)

myField.field.exitonclick()
