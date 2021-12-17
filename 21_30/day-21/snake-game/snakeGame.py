from turtle import Turtle, Screen


class snake_game:

    def __init__(self):
        self.screen = Screen()
        self.snake = []

    def init_screen(self):
        self.screen.setup(height=600, width=600)
        self.screen.bgcolor('black')
        self.screen.title('SNAKE GAME')
        self.screen.tracer(0)  # To update screen only when desired

    def init_snake(self):
        new_segment = Turtle('arrow')
        new_segment.fillcolor('white')
        new_segment.penup()
        self.snake.append(new_segment)
        self.screen.update()

    def init_game(self):
        """This will initialise the game with a snake of length 1"""
        self.init_screen()
        self.init_snake()
        self.bind_keys()

    def add_to_snake(self):
        """This will add a segment to the snake (increase snake length by 1)"""
        new_segment = Turtle('square')
        new_segment.fillcolor('white')
        new_segment.penup()
        prev_segment = self.snake[-1]
        head_dir = self.snake[0].heading()
        if head_dir == 0:
            new_segment.goto(prev_segment.xcor() - 20, prev_segment.ycor())
        elif head_dir == 90:
            new_segment.goto(prev_segment.xcor(), prev_segment.ycor() - 20)
        elif head_dir == 180:
            new_segment.goto(prev_segment.xcor() - 20, prev_segment.ycor())
        elif head_dir == 270:
            new_segment.goto(prev_segment.xcor(), prev_segment.ycor() + 20)
        self.snake.append(new_segment)
        self.screen.update()

    def move(self, direction):
        for i in range(len(self.snake) - 1, 0, -1):
            cur_segment = self.snake[i]
            prev_segment = self.snake[i - 1]
            cur_segment.goto(prev_segment.xcor(), prev_segment.ycor())
        head = self.snake[0]
        if direction == 'forward':
            head.forward(20)
        elif direction == 'up':
            if not head.heading() == 270:
                head.setheading(90)
                head.forward(20)
        elif direction == 'down':
            if not head.heading() == 90:
                head.setheading(270)
                head.forward(20)
        elif direction == 'left':
            if not head.heading() == 0:
                head.setheading(180)
                head.forward(20)
        elif direction == 'right':
            if not head.heading() == 180:
                head.setheading(0)
                head.forward(20)
        self.screen.update()

    def reset_snake(self):
        for segments in self.snake:
            segments.reset()

    def move_up(self):
        self.move('up')

    def move_down(self):
        self.move('down')

    def move_left(self):
        self.move('left')

    def move_right(self):
        self.move('right')

    def bind_keys(self):
        """This will bind keypress events to the screen"""
        self.screen.listen()
        self.screen.onkeypress(self.move_up, 'Up')
        self.screen.onkeypress(self.move_down, 'Down')
        self.screen.onkeypress(self.move_left, 'Left')
        self.screen.onkeypress(self.move_right, 'Right')
