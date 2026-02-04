from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10  # KEY CONCEPT: Tuning constant for difficulty progression


class CarManager():

    def __init__(self) -> None:
        # PATTERN: Maintain list of all active game objects
        # This allows scalable iteration: works with 5 cars or 50 cars
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # PATTERN: Random object spawning creates organic, unpredictable gameplay
        # Without this, patterns would be predictable and memorizable
        random_chance = random.randint(1, 6)
        if random_chance == 1:  # 1 in 6 chance each frame (16.7% spawn rate)
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))  # See Day 5: random selection
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)  # Start at right side of screen
            self.all_cars.append(new_car)  # Add to collection for movement

    def move_cars(self):
        # PATTERN: Update all objects in collection
        # This scales elegantly - same code works for any number of cars
        # Movement is controlled by self.car_speed which increases each level
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        # PATTERN: Linear difficulty scaling
        # Each level increases speed by fixed amount (10 pixels/frame)
        # Level 1: 5, Level 2: 15, Level 3: 25, etc.
        self.car_speed += MOVE_INCREMENT
        # NOTE: Could optimize by capping speed to prevent impossible levels
        # Example: self.car_speed = min(self.car_speed + MOVE_INCREMENT, 20)