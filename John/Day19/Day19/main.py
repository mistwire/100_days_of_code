import turtle
from turtle import Turtle, Screen
import random


turtle.mode()
screen = Screen()
screen.setup(width=500, height=400)
walk_speed = 10
finish_line = 225
win_color = ""

# Draw Finish Line
pacer_turtle = Turtle(shape="turtle")
pacer_turtle.hideturtle()
pacer_turtle.penup()
pacer_turtle.goto(x=finish_line, y =-110)
pacer_turtle.pendown()
pacer_turtle.goto(x=finish_line, y=175)
pacer_turtle.penup()


user_bet = turtle.textinput(title="Choose your turtle!", prompt="Which one will win? ")
#print(user_bet)
colors = ["red","orange","yellow","green","blue","purple"]
starting_y = -100
starting_x = -225
turtles = []

def generate_turtle(index, t_color, x, y):
    #print(f"Index is {index}, color is {t_color}")

    turtles.append(Turtle(shape="turtle"))

    turtles[index].color(t_color)
    turtles[index].penup()
    turtles[index].goto(x=x, y=y)

def walk_turtles():
    win_color = ""
    for walking_turtle in turtles:
        walking_turtle.forward(distance=(random.randrange(0, walk_speed)))
        if walking_turtle.xcor() >= finish_line:
            win_color = walking_turtle.color()
            #print(win_color)
    return win_color


for _ in range(len(colors)):
    #print(colors[_])
    generate_turtle(index=_, t_color=colors[_], x=starting_x, y=starting_y)
    starting_y += 50


while True:
    won = walk_turtles()
    if won:
        break


print(f"The WINNER is {won[0]}!")
if user_bet == won[0]:
    print("You win!!")
else:
    print("Sorry, you lose.  :-( ")










# for turtle in turtles:
#     turtle.pen()
#     turtle.goto(x=starting_x, y=starting_y)

screen.exitonclick()