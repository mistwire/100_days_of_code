import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
# Make the gif a variable:
image = "blank_states_img.gif"
# Load image as a turtle shape:
screen.addshape(image)
correct_guesses = 0
# Now available to be used by a turtle:
turtle.shape(image)

df = pandas.read_csv("50_states.csv")
all_states = df.state.to_list()
guessed_states = []


def write_state(state_name, x, y):
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.goto(x, y)
    t.write(state_name)


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States", prompt="Input state name").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        df_out = pandas.DataFrame(missing_states, columns='state')
        df_out.to_csv('states_to_learn.csv')
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = df[df.state == answer_state]
        write_state(answer_state, int(state_data.x) - 20, int(state_data.y))

screen.exitonclick()

