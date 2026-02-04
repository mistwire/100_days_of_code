import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # PATTERN: Spawn and move cars each frame
    # Random spawning + iteration over collection
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with any car
    # KEY CONCEPT: Iterate through car_manager.all_cars which grows each level
    # All cars on screen are checked, regardless of how many there are
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect success (player reached finish line)
    # PATTERN: Win condition triggers level progression
    if player.is_at_finish_line():
        player.go_to_start()        # Reset player position
        car_manager.level_up()      # Increase difficulty
        scoreboard.increase_level() # Update display
        # NOTE: Cars are NOT cleared - they continue moving from level to level
        # This creates cascading difficulty (old cars stay, new ones spawn faster)


screen.exitonclick()