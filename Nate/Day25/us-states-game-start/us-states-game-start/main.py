import turtle
import pandas as pd

image = "blank_states_img.gif"
states_file = "50_states.csv"

screen = turtle.Screen()
screen.title("US States Game")
screen.bgpic(image)
# screen.addshape(image)
# turtle.shape(image)
turtle.penup()
turtle.hideturtle()
correct = 0
game_on = True

df = pd.read_csv(states_file)

while game_on:
    attempt = screen.textinput(title=f"{correct}/50 correct", prompt="Enter name of a US state")
    state = df[df.state == attempt]
    
    if len(state) > 0:
        x_cord = df[df.state == attempt].x.item()
        y_cord = df[df.state == attempt].y.item()
        turtle.goto(x_cord, y_cord)
        turtle.write(attempt, move=True)
        correct += 1

screen.exitonclick()
