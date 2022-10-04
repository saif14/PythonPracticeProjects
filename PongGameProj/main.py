from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game!")
screen.listen()
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkeypress(paddle_r.up, "Up")
screen.onkeypress(paddle_r.down, "Down")

screen.onkeypress(paddle_l.up, "w")
screen.onkeypress(paddle_l.down, "s")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collison with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collison with right paddle
    if (ball.distance(paddle_r) < 50 and ball.xcor() > 320) or (ball.distance(paddle_l) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect Right Paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_l_score()
        scoreboard.update_score_board()

    # Detect Left Paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_r_score()
        scoreboard.update_score_board()
screen.exitonclick()
