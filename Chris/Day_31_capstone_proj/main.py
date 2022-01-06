import tkinter
import random

BACKGROUND_COLOR = "#B1DDC6"








# ---------------------------- UI SETUP ------------------------------- #

gui = tkinter.Tk()
gui.title("Flashy")
gui.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

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


gui.mainloop()

