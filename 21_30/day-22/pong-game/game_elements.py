from turtle import Turtle


class GameElements:

    def __init__(self, element_type, player_speed=0):
        self.element = Turtle()
        self.player_speed = player_speed
        if element_type == 'paddle':
            self.element.color('white')
            self.element.shape('square')
            self.element.shapesize(stretch_wid=1, stretch_len=6)
            self.element.setheading(90)
            self.element.penup()
        elif element_type == 'ball':
            self.element.color('white')
            self.element.shape('circle')
            self.element.penup()

    def set_pos(self, player_number):
        """Set the element's initial position depending on element type"""
        self.element.speed('fastest')
        if player_number == 1:
            self.element.goto(-550, 0)
        elif player_number == 2:
            self.element.goto(550, 0)
        elif player_number == 0:
            self.element.goto(0, 0)

    def init_game(self, player_number):
        """Initialize the game by setting elements' initial values"""
        self.set_pos(player_number)

    def moveup(self):
        self.element.setheading(90)
        self.element.forward(self.player_speed)

    def movedown(self):
        self.element.setheading(-90)
        self.element.forward(self.player_speed)
