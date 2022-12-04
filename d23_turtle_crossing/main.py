import time
import random
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.go_left()
    new_car_decision = random.random()
    if new_car_decision > 0.8:
        cars.add_car()

    for car in cars.cars:
        if car.distance(player) < 20:
            game_is_on = False

    if player.is_at_finish_line():
        player.player_reset()
        cars.level_up()
        scoreboard.update_level()

screen.update()
screen.exitonclick()