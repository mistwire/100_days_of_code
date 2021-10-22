import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
scoreboard = Scoreboard()
cars = []

screen.onkey(player.move, "Up")

# random number of cars
for _ in range(10):
    car = CarManager()
    cars.append(car)

game_is_on = True
while game_is_on:
    scoreboard.update_scoreboard()
    for car in cars:
        car.move()

        if player.distance(car) <= 20 and player.ycor() == car.ycor():
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() == 280:
        scoreboard.level += 1
        for car in cars:
            car.speed_up()
        player.reset()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
