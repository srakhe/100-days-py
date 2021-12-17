from turtle import Turtle


class score_board(Turtle):

    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.write(f'Score: {self.score}', move=False, align="left", font=("Arial", 9, "bold"))

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', move=False, align="left", font=("Arial", 9, "bold"))

    def game_over(self):
        self.clear()
        self.score += 1
        self.write(f'Game Over! Final Score: {self.score}', move=False, align="center", font=("Arial", 15, "bold"))
