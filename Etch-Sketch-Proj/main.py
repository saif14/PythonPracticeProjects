from turtle import Turtle, Screen

arrow = Turtle()
screen = Screen()


def move_forward():
    arrow.forward(5)


def move_backward():
    arrow.backward(5)


def clockwise():
    arrow.setheading(arrow.heading()-10)


def anticlock():
    arrow.setheading(arrow.heading()+10)


def clear():
    arrow.penup()
    arrow.clear()
    arrow.home()
    arrow.pendown()

screen.listen()
screen.onkeypress(key="Right", fun=move_forward)
screen.onkeypress(key="Left", fun=move_backward)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="a", fun=anticlock)
screen.onkeypress(key="c", fun=clear)
screen.exitonclick()
