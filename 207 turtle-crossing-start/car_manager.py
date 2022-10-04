from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.move_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1,7)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.move_speed = STARTING_MOVE_DISTANCE
            # x_cor = random.randint(x_cor_limit[0], x_cor_limit[1])
            y_cor = random.randint(-250, 250)
            # print(x_cor, y_cor, new_car.color())
            new_car.goto(305, y_cor)
            self.all_cars.append(new_car)

    def move_cars(self):
        # self.move_speed += MOVE_INCREMENT
        for car in self.all_cars:
            car.backward(self.move_speed)

    def increase_car_movement(self):
        self.move_speed += MOVE_INCREMENT
