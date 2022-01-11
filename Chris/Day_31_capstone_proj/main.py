import tkinter
import pandas
import random
from os.path import exists


BACKGROUND_COLOR = "#B1DDC6"

# grab the data using pandas:
if exists("data/words_to_learn.csv"):
    data = pandas.read_csv("data/words_to_learn.csv")
else:
    data = pandas.read_csv("data/french_words.csv")
# turn it into a dict w/ the 'records' orientation
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
to_learn = data.to_dict(orient="records")
current_card = {}


def know_word():
    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def next_card():
    global current_card, flip_timer
    gui.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    flip_timer = gui.after(3000, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(card_background, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")


# ---------------------------- UI SETUP ------------------------------- #

gui = tkinter.Tk()
gui.title("Flashy")
gui.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = gui.after(3000, func=flip_card)

# images
card_front_image = tkinter.PhotoImage(file="images/card_front.png")
card_back_image = tkinter.PhotoImage(file="images/card_back.png")
wrong_image = tkinter.PhotoImage(file="images/wrong.png")
right_image = tkinter.PhotoImage(file="images/right.png")


# Canvas
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front_image)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Buttons
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_button = tkinter.Button(image=right_image, highlightthickness=0)
right_button.grid(column=1, row=1)

next_card()

gui.mainloop()

