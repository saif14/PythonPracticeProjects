from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make Your Bet", prompt="Which tutle will win the race? Enter a color: ")
print(user_bet)
is_race_on = False

turtle_list = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = -120

for idx in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[idx])
    new_turtle.goto(-230, y_pos)
    turtle_list.append(new_turtle)

    y_pos += 50

if user_bet:
    is_race_on = True

winning_turtle_color = ""

while is_race_on:
    for turtle in turtle_list:
        turtle.forward(random.randint(0, 10))
        if turtle.pos()[0] >= 240:
            is_race_on = False
            winning_turtle_color = turtle.color()[0]
            print(winning_turtle_color)

if winning_turtle_color == user_bet:
    turtle = Turtle()
    turtle.hideturtle()
    turtle.penup()
    turtle.write(f"You Win! Winner Turtle is {winning_turtle_color.upper()}", font=("Verdana", 24, "bold"), align="center")
else:
    turtle = Turtle()
    turtle.hideturtle()
    turtle.penup()
    turtle.write(f"You Loose! Winner Turtle is {winning_turtle_color.upper()}", font=("Verdana", 18, "bold"), align="center")

screen.exitonclick()
