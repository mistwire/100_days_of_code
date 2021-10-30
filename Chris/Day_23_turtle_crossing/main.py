import time
import turtle
import player
import car_manager
import scoreboard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = player.Player()
car_manager = car_manager.CarManager()
scoreboard = scoreboard.Scoreboard()

screen.listen()
# No () in onkey - only want it to trigger when "Up" is pressed:
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
# Detect turtle + car collision
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False
    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level_up()

screen.exitonclick()
