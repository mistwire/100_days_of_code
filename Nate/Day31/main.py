from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_CSV = "data/spanish_1000words.csv"
word_dict = {}
random_word = None
missed_words = []
counting = False


def card_flip():
    card_canvas.itemconfig(canvas_image, image=card_back_img)
    card_canvas.itemconfig(card_title, fill="white", text="English")
    card_canvas.itemconfig(card_word, fill="white", text=random_word["Translation"])


def import_data():
    global word_dict
    try:
        df = pd.read_csv("data/words_to_learn.csv")
        word_dict = df.to_dict(orient="records")
    except FileNotFoundError:
        df = pd.read_csv(LANGUAGE_CSV)
        word_dict = df.to_dict(orient="records")


def random_card():
    global random_word
    global timer
    window.after_cancel(timer)
    random_word = random.choice(word_dict)
    card_canvas.itemconfig(canvas_image, image=card_front_img)
    card_canvas.itemconfig(card_title, text="Spanish", fill="black")
    card_canvas.itemconfig(card_word, text=random_word["Word"], fill="black")
    timer = window.after(3000, card_flip)


def press_x():
    random_card()


def press_y():
    global word_dict
    word_dict = [word for word in word_dict if not (word["Word"] == random_word["Word"])]
    new_df = pd.DataFrame(word_dict)
    new_df.to_csv("data/words_to_learn.csv", index=False)
    random_card()


# ---------------------------- UI  ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_canvas.config(highlightthickness=0)
card_canvas.grid(row=0, column=0, columnspan=2)

x_button_img = PhotoImage(file="images/wrong.png")
x_button_label = Label(image=x_button_img)
x_button = Button(image=x_button_img, borderwidth=0, highlightthickness=0, command=press_x)
x_button.grid(row=1, column=0)

y_button_img = PhotoImage(file="images/right.png")
y_button_label = Label(image=y_button_img)
y_button = Button(image=y_button_img, borderwidth=0, highlightthickness=0, command=press_y)
y_button.grid(row=1, column=1)

# ---------------------------- Card Elements  ------------------- #


import_data()
canvas_image = card_canvas.create_image(400, 260, image=card_front_img)
card_title = card_canvas.create_text(400, 150, text="Spanish", fill="black", font=("arial", 30, "italic"))
card_word = card_canvas.create_text(400, 250, text="", fill="black", font=("arial", 30, "bold"))
timer = window.after(3000, card_flip)
random_card()


window.mainloop()
