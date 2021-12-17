from turtle import Turtle
import random

colors = ['red', 'orange', 'blue', 'black', 'yellow', 'gray', 'pink', 'purple']
MAX_X = 0
MAX_Y = 0


def init_car_pos(car):
    x_cor = random.randint(MAX_X - 50, MAX_X)
    y_cor = random.randint(-MAX_Y, MAX_Y)
    car.goto(x_cor, y_cor)


class CarsGen:

    def __init__(self, num_cars, max_x, max_y):
        global MAX_X, MAX_Y, colors
        self.cars = []
        for i in range(0, num_cars):
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(colors))
            new_car.penup()
            new_car.speed('fastest')
            self.cars.append(new_car)
        MAX_X = max_x
        MAX_Y = max_y - 80

    def init_all_cars(self):
        for car in self.cars:
            x_cor = random.randint(MAX_X - 50, MAX_X)
            y_cor = random.randint(-MAX_Y, MAX_Y)
            car.goto(x_cor, y_cor)

    def move_cars(self, level):
        for car in self.cars:
            car.goto(car.xcor() - random.randint(level * 20, level * 21), car.ycor())
            if car.xcor() <= -(MAX_X - 20):
                init_car_pos(car)

    def hits(self, turtle_to_check):
        for car in self.cars:
            print(car.distance(turtle_to_check))
            if car.distance(turtle_to_check) < 40:
                return True
        return False
