import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
color_list = [(240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
arrow = Turtle()
arrow.speed(10)
arrow.hideturtle()
# arrow.setheading(225)
arrow.penup()
arrow.goto((-247.49,-247.49))
number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    # for _ in range(1,10):
    arrow.dot(15, random.choice(color_list))
    arrow.forward(50)
    if dot_count %10 == 0:
        arrow.setheading(90)
        arrow.forward(50)
        arrow.setheading(180)
        arrow.forward(500)
        arrow.setheading(0)

scr = Screen()
scr.exitonclick()


