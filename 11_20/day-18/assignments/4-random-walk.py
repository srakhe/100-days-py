from turtle import Turtle, Screen
import random

choices = [0, 90, -90, 180, -180, 270, -270, 360]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


def random_walk(my_turtle):
    my_turtle.pensize(6)
    my_turtle.speed(0)
    while my_turtle.xcor() < 450 and my_turtle.xcor() > -450 and my_turtle.ycor() < 450 and my_turtle.ycor() > -450:
        my_turtle.setheading(my_turtle.heading() + random.choice(choices))
        my_turtle.forward(25)
        my_turtle.color(random.choice(colours))


my_turtle = Turtle()
my_turtle.shape('turtle')

random_walk(my_turtle)

screen = Screen()
screen.exitonclick()
