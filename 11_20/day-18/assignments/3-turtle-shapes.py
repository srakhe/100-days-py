from turtle import Turtle, Screen


def shape(my_turtle, num_sides, side_len):
    exterior_angle = 360 / num_sides
    for _ in range(0, num_sides):
        my_turtle.forward(side_len)
        my_turtle.setheading(my_turtle.heading() + exterior_angle)


my_turtle = Turtle()
my_turtle.shape('turtle')

for i in range(3, 11):
    shape(my_turtle, i, 50)
    my_turtle.clear()

screen = Screen()
screen.exitonclick()
