from turtle import Turtle
from scoreboard import Scoreboard
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 5
scoreboard = Scoreboard()


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.current_level = 1
        self.car_segments = []
        self.create_car()

    def create_car(self):
        if random.randint(0, 15 - self.current_level) < 7:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(310, random.randint(-235, 300))
            new_car.color(random.choice(COLORS))
            self.car_segments.append(new_car)
        self.move_car()

    def move_car(self):
        for seg_num in range(0, (len(self.car_segments))):
            self.car_segments[seg_num].setheading(180)
            self.car_segments[seg_num].forward(STARTING_MOVE_DISTANCE + self.current_level * MOVE_INCREMENT)

    def update_car_speed(self, level):
        self.current_level += 1
