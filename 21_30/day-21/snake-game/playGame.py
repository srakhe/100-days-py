from snakeGame import snake_game
from food import Food
from scoreBoard import score_board
import time

mySnakeGame = snake_game()
myFood = Food()
scoreB = score_board()

mySnakeGame.init_game()
mySnakeGame.bind_keys()

gameOver = False
while not gameOver:
    mySnakeGame.move('forward')
    time.sleep(0.1)

    if mySnakeGame.snake[0].distance(myFood) < 20:
        myFood.refresh()
        scoreB.add_score()
        mySnakeGame.add_to_snake()

    if mySnakeGame.snake[0].xcor() > 280 or mySnakeGame.snake[0].xcor() < -280 or mySnakeGame.snake[0].ycor() > 280 or \
            mySnakeGame.snake[0].ycor() < -280:
        gameOver = True
        mySnakeGame.reset_snake()
        scoreB.game_over()

    for segments in mySnakeGame.snake[1:]:
        if mySnakeGame.snake[0].distance(segments) < 15:
            gameOver = True
            mySnakeGame.reset_snake()
            scoreB.game_over()

mySnakeGame.screen.exitonclick()
