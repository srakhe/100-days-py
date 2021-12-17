from turtle import Turtle, Screen
import colorgram
import random

color_list = []


def get_colors():
    colors = colorgram.extract('image.jpg', 30)
    for color in colors:
        colour_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
        color_list.append(colour_tuple)


def paint(my_turtle):
    my_turtle.speed(0)
    my_turtle.penup()
    my_turtle.sety(-300)
    my_turtle.pendown()
    for i in range(0, 10):
        my_turtle.penup()
        my_turtle.setx(-300)
        my_turtle.pendown()
        for j in range(0, 10):
            color = random.choice(color_list)
            my_turtle.pen(pencolor='white', fillcolor=color)
            my_turtle.begin_fill()
            my_turtle.circle(radius=10)
            my_turtle.end_fill()
            my_turtle.penup()
            my_turtle.setx(my_turtle.xcor() + 50)
            my_turtle.pendown()
        my_turtle.penup()
        my_turtle.sety(my_turtle.ycor() + 50)
        my_turtle.pendown()


my_turtle = Turtle()
my_turtle.shape('turtle')
screen = Screen()

get_colors()
screen.colormode(255)
paint(my_turtle)

screen.exitonclick()
