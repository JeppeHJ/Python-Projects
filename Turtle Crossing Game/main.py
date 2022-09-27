import time
from turtle import Screen
from player import Player
import random
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.listen()
player = Player()
screen.onkeypress(player.move_up, "w")
screen.setup(width=600, height=600)

car = CarManager()
scoreboard = Scoreboard()

current_level = 1

game_is_on = True

while game_is_on:
    screen.update()
    car.create_car()
    time.sleep(0.1)
    for unit in range(0, len(car.car_segments)):
        if player.distance(car.car_segments[unit]) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() >= 290:
        current_level += 1
        car.update_car_speed(current_level)
        player.goto(0, -280)
        scoreboard.score()

screen.exitonclick()