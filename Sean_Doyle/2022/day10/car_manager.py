from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self, level):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * level))

    def check_hit(self, player):
        for car in self.all_cars:
            if (
                abs(car.xcor() - player.xcor()) < 20
                and abs(car.ycor() - player.ycor()) < 10
            ):
                return True
