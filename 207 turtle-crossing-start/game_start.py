import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


class GameStart:
    def __init__(self):
        self.screen = Screen()
        self.player = Player()
        self.car_manager = CarManager()
        self.scoreboard = Scoreboard()
        self.is_game_on = False

    def setup_screen(self):
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)
        self.screen.listen()

    def start_game(self):
        self.screen.onkeypress(self.player.move_turtle, "Up")

        self.is_game_on = True
        game_is_on = True
        while self.is_game_on:
            time.sleep(0.1)
            # time.sleep(2)
            self.screen.update()
            self.car_manager.create_car()
            self.car_manager.move_cars()

            # Detect collision with car
            for car in self.car_manager.all_cars:
                if car.distance(self.player) < 20:
                    self.is_game_on = False
                    self.scoreboard.game_over()

            # Detect successful crossing
            if self.player.is_at_finish_line():
                self.player.goto_start()
                self.car_manager.increase_car_movement()
                self.scoreboard.increase_level()

        self.screen.exitonclick()


# screen = Screen()
# screen.setup(width=600, height=600)
# screen.tracer(0)
# screen.listen()

# player = Player()
# car_manager = CarManager()
# scoreboard = Scoreboard()

# screen.onkeypress(player.move_turtle, "Up")
#
# game_is_on = True
# while game_is_on:
#     time.sleep(0.1)
#     # time.sleep(2)
#     screen.update()
#     car_manager.create_car()
#     car_manager.move_cars()
#
#     # Detect collision with car
#     for car in car_manager.all_cars:
#         if car.distance(player) < 20:
#             game_is_on = False
#             scoreboard.game_over()
#
#     # Detect successful crossing
#     if player.is_at_finish_line():
#         player.goto_start()
#         car_manager.increase_car_movement()
#         scoreboard.increase_level()
#
# screen.exitonclick()