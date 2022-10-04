from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.goto(random.randint(-230, 230), random.randint(-230, 230))

    def refresh(self):
        self.goto(random.randint(-230, 230), random.randint(-230, 230))
