from turtle import Turtle, Screen
from random import choice

screen = Screen()
screen.setup(width=500, height=400)

bet = screen.textinput(title="Make a bet", prompt="Choose a color")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y_position = -100

for color in colors:
    t = Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(-230, y_position)
    turtles.append(t)
    y_position += 50


movement_choice = (2, 5, 10)

winner = False
while not winner:
    for turtle in turtles:
        turtle.forward(choice(movement_choice))
        if turtle.xcor() > 220:
            print(f"The {turtle.color()[0]} turtle is the winner!")
            print("You won the bet!" if bet == turtle.color()[0] else "You lost the bet.")
            winner = True





screen.exitonclick()
