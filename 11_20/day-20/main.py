from snakeGame import snakeGame

mySnakeGame = snakeGame()

mySnakeGame.init_game()
mySnakeGame.bind_keys()

mySnakeGame.play_game()

mySnakeGame.screen.exitonclick()
