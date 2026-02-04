import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=800, height=650)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# PATTERN: Read state data from CSV (state name, x coordinate, y coordinate)
data = pandas.read_csv("50_states.csv")

# KEY CONCEPT: Convert DataFrame column to list for membership checking
# to_list() extracts Series into Python list for fast `in` operations
all_states = data.state.to_list()

# Track game progress
guessed_states = []

while len(guessed_states) < 50:
    # PATTERN: Use game progress in UI feedback
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states guessed",
                                    prompt="What's another state name?").title()

    # Win condition: exit early and save states to learn
    if answer_state == "Exit":
        # PATTERN: List comprehension for filtering (Day 26 preview)
        # Find states NOT in guessed list - these are the ones to study
        states_to_learn = [state for state in all_states if state not in guessed_states]

        # PATTERN: Convert list back to DataFrame for CSV output
        # pandas.DataFrame(list_data) creates single-column DataFrame
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("state_to_learn.csv")
        break

    # Check if answer is valid state name
    if answer_state in all_states:
        guessed_states.append(answer_state)

        # PATTERN: Filter DataFrame to get single state's data
        state_data = data[data.state == answer_state]

        # Create turtle for displaying state name on map
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        # KEY CONCEPT: Extract coordinates using .item()
        # .x returns Series (could have multiple values)
        # .item() extracts the single value as scalar
        # int() converts string to integer for goto()
        t.goto(int(state_data.x.item()), int(state_data.y.item()))

        # Write state name on map at correct position
        t.write(state_data.state.item())

turtle.mainloop()