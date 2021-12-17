from turtle import Screen, Turtle

MAX_X = 0
MAX_Y = 0


class GameScreen():

    def __init__(self, max_x, max_y):
        super().__init__()
        global MAX_X, MAX_Y
        MAX_X = max_x
        MAX_Y = max_y
        self.screen = Screen()
        self.screen.setup(height=max_x, width=max_y)
        self.screen.bgcolor('white')
        self.screen.title('Crossing Game')
        self.level_turtle = Turtle()
        self.level_turtle.penup()
        self.level_turtle.speed('fastest')
        self.level_turtle.goto(MAX_X - 50, MAX_Y - 50)
        self.level_turtle.hideturtle()

    def bind_keys(self, obj):
        """Bind the keys to the screen"""
        self.screen.listen()
        self.screen.onkeypress(obj.move_up, 'Up')
        self.screen.onkeypress(obj.move_down, 'Down')

    def draw_border(self):
        """Draw the border to the game (Start and finish line as well)"""
        border_turtle = Turtle()
        border_turtle.color('black')
        border_turtle.speed('fastest')
        border_turtle.hideturtle()
        border_turtle.penup()
        border_turtle.goto(-MAX_X, MAX_Y)
        border_turtle.pendown()
        border_turtle.goto(MAX_X, MAX_Y)
        border_turtle.goto(MAX_X, -MAX_Y)
        border_turtle.goto(-MAX_X, -MAX_Y)
        border_turtle.goto(-MAX_X, MAX_Y)
        border_turtle.penup()
        border_turtle.goto(0, MAX_Y)
        border_turtle.write('FINISH', move=False, align='center', font=("Arial", 20, "bold"))

    def update_level(self, level):
        """Display level in game"""
        self.level_turtle.clear()
        self.level_turtle.write(f'Level: {level}', move=False, align='center', font=("Arial", 10, "bold"))
