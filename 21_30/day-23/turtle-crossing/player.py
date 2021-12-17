from turtle import Turtle

MAX_X = 0
MAX_Y = 0
DIST_TRAVEL = 0


class Player(Turtle):

    def __init__(self, max_x, max_y, dist_travel):
        super().__init__()
        global MAX_X, MAX_Y, DIST_TRAVEL
        self.penup()
        self.shape('turtle')
        self.color('green')
        self.speed('fastest')
        self.goto(0, -max_y)
        self.setheading(90)
        MAX_X = max_x
        MAX_Y = max_y
        DIST_TRAVEL = dist_travel

    def move_up(self):
        self.goto(0, self.ycor() + DIST_TRAVEL)

    def move_down(self):
        self.goto(0, self.ycor() - DIST_TRAVEL)
