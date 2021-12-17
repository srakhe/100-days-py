from turtle import Turtle


class ScoreBoard:

    def __init__(self, side, max_y):
        self.score = 0
        self.scoreTurtle = Turtle()
        self.scoreTurtle.penup()
        self.scoreTurtle.color('white')
        self.scoreTurtle.hideturtle()
        self.side = side
        if side == 'l':
            self.scoreTurtle.goto(-50, (max_y - 50))
            self.scoreTurtle.write('0', move=False, align="left", font=("Arial", 20, "bold"))
        elif side == 'r':
            self.scoreTurtle.goto(50, (max_y - 50))
            self.scoreTurtle.write('0', move=False, align="right", font=("Arial", 20, "bold"))

    def add_score(self):
        """Increase the score displayed"""
        self.scoreTurtle.clear()
        self.score += 1
        if self.side == 'l':
            self.scoreTurtle.write(self.score, move=False, align="left", font=("Arial", 20, "bold"))
        elif self.side == 'r':
            self.scoreTurtle.write(self.score, move=False, align="right", font=("Arial", 20, "bold"))
