from game_start import GameStart
# import time
# from turtle import Screen
# from player import Player
# from car_manager import CarManager
# from scoreboard import Scoreboard
#
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.tracer(0)
# screen.listen()
#
# player = Player()
# car_manager = CarManager()
# scoreboard = Scoreboard()
#
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


game_start = GameStart()
game_start.setup_screen()
game_start.start_game()


