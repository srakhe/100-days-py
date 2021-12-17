from turtle import Turtle, Screen


def dashed_line(my_turtle, distance):
    dist_travelled = 0
    while dist_travelled < distance:
        my_turtle.forward(5)
        dist_travelled += 5
        my_turtle.penup()
        my_turtle.forward(5)
        dist_travelled += 5
        my_turtle.pendown()


def dashed_square(my_turtle):
    for i in range(0, 4):
        my_turtle.setheading(my_turtle.heading() + 90)
        dashed_line(my_turtle, 100)


my_turtle = Turtle()
my_turtle.shape('turtle')

dashed_square(my_turtle)

screen = Screen()
screen.exitonclick()
