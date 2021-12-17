from turtle import Screen, Turtle


class PongField:

    def __init__(self, mx, my):
        self.field = Screen()
        self.max_x = mx
        self.max_y = my
        self.field.setup(width=self.max_x, height=self.max_y)
        self.field.title('Pong Game')
        self.field.bgcolor('black')

    def bind_keys(self, player1, player2):
        """Bind keys to screen to play the game"""
        self.field.listen()
        self.field.onkeypress(player1.moveup, 'w')
        self.field.onkeypress(player1.movedown, 's')
        self.field.onkeypress(player2.moveup, 'Up')
        self.field.onkeypress(player2.movedown, 'Down')

    def draw_border(self):
        """Draw the screen border for the game"""
        temp_turtle = Turtle()
        temp_turtle.hideturtle()
        temp_turtle.color('white')
        temp_turtle.speed('fastest')
        # start drawing from top left corner
        temp_turtle.penup()
        temp_turtle.goto(-self.max_x, self.max_y)
        temp_turtle.pendown()
        temp_turtle.goto(self.max_x, self.max_y)
        temp_turtle.goto(self.max_x, -self.max_y)
        temp_turtle.goto(-self.max_x, -self.max_y)
        temp_turtle.goto(-self.max_x, self.max_y)
        # draw the center line
        temp_turtle.goto(0, self.max_y)
        while temp_turtle.ycor() > -self.max_y:
            temp_turtle.pendown()
            temp_turtle.goto(0, temp_turtle.ycor() - 20)
            temp_turtle.penup()
            temp_turtle.goto(0, temp_turtle.ycor() - 20)
        temp_turtle.penup()
