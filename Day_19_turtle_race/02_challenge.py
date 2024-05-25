from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bets = screen.textinput(title="Make Your Bets!", prompt="Which turtle color will win the race?")
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
starting_y_positions = [-70, -40, -10, 20, 50, 80]
race_running = False
all_turtles = []


for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, starting_y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bets:
    race_running = True

while race_running:
    for turtle in all_turtles:
        if turtle.xcor() >=230:
            race_running = False
            winning_color = turtle.pencolor()
            if winning_color == user_bets:
                print(f"You've won! The {winning_color} turtle has won!")
            else:
                print(f"You've lost! The {winning_color} turtle has won!")

        
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()