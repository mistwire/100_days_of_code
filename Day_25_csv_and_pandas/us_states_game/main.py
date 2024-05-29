import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=800, height=650)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states guessed", 
                                    prompt="What's another state name?").title()


    if answer_state == "Exit":
        states_to_learn = [state for state in all_states if state not in guessed_states]
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("state_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(state_data.state.item())

turtle.mainloop()