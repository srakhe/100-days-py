from turtle import Turtle, Screen
import random


def spirograph(my_turtle):
    my_turtle.speed(0)
    current_angle = my_turtle.heading()
    while current_angle < 360:
        my_turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        my_turtle.circle(radius=100)
        current_angle += 10
        my_turtle.setheading(current_angle)


my_turtle = Turtle()
my_turtle.shape('turtle')
screen = Screen()

screen.colormode(255)
spirograph(my_turtle)

screen.exitonclick()
