from turtle import Turtle, Screen


def square(my_turtle):
    for i in range(0, 4):
        my_turtle.setheading(my_turtle.heading() + 90)
        my_turtle.forward(100)


my_turtle = Turtle()
my_turtle.shape('turtle')

square(my_turtle)

screen = Screen()
screen.exitonclick()
