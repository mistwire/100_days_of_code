import turtle
import pandas as pd

image = "blank_states_img.gif"
states_file = "50_states.csv"
not_found_file = "not_found.csv"

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
all_states = df.state.to_list()
states_found = []

while game_on:
    attempt = screen.textinput(title=f"{correct}/50 correct", prompt="Enter name of a US state")

    if attempt == "Exit":
        break

    if attempt in all_states:
        state = df[df.state == attempt]
        states_found.append(attempt)
        x_cord = int(state.x)
        y_cord = int(state.y)
        turtle.goto(x_cord, y_cord)
        turtle.write(state.state.item())
        correct += 1

states_not_found = all_states.copy()

for i in states_found:
    if i in states_not_found:
        states_not_found.remove(i)

df = pd.DataFrame(states_not_found, columns=["States Not Found"])
df.to_csv(not_found_file, index=False)

print(states_not_found)