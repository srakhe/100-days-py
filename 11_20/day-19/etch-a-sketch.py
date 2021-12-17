from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()
my_turtle.shape('arrow')


def forward():
    my_turtle.forward(10)


def backward():
    my_turtle.back(10)


def right():
    my_turtle.right(10)


def left():
    my_turtle.left(10)

def clear_screen():
    my_turtle.penup()
    my_turtle.home()
    my_turtle.clear()
    my_turtle.pendown()

screen.listen()
screen.onkeypress(forward, 'w')
screen.onkeypress(backward, 's')
screen.onkeypress(right, 'd')
screen.onkeypress(left, 'a')
screen.onkeypress(clear_screen, 'c')

screen.exitonclick()
