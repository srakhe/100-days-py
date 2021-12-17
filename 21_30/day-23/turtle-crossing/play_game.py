import time

from cars_gen import CarsGen
from player import Player
from game_screen import GameScreen

NUMBER_CARS = 8
DISTANCE_TRAVEL = 20
MAX_X = 600
MAX_Y = 400

traffic = CarsGen(num_cars=NUMBER_CARS, max_x=MAX_X, max_y=MAX_Y)
player = Player(dist_travel=DISTANCE_TRAVEL, max_x=MAX_X, max_y=MAX_Y)
my_screen = GameScreen(max_x=MAX_X, max_y=MAX_Y)
my_screen.bind_keys(player)
my_screen.draw_border()

traffic.init_all_cars()

level = 1
game_over = False
my_screen.update_level(level)
while not game_over:
    traffic.move_cars(level)
    if player.ycor() >= MAX_Y:
        player.goto(0, -MAX_Y)
        level += 1
        my_screen.update_level(level)
    if traffic.hits(player):
        game_over = True
    time.sleep(0.1)
my_screen.screen.exitonclick()
