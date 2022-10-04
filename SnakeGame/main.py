from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard

from food import Food
from snake import Snake

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

is_game_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()
# scoreboard.show_score(scoreboard.score)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()

    #Detect collision with wall
    if snake.head.xcor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
        is_game_on = False
        scoreboard.game_over()


screen.exitonclick()
