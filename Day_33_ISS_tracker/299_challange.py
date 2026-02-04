from tkinter import *  # PATTERN: Tkinter for GUI (see Day 27)
import requests


def get_quote():
    # API: Fetch random Kanye West quote from free public API
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    ye_sez = response.json()['quote']  # KEY CONCEPT: Extract single field from JSON response
    canvas.itemconfig(quote_text, text=ye_sez)  # Update canvas text dynamically


# PATTERN: tkinter GUI setup (see Day 27_Tkinter)
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Canvas for displaying quote over background image
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207,
                                text="Kanye Quote Goes HERE",
                                width=250,
                                font=("Arial", 30, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

# Button that calls get_quote when clicked (callback pattern, see Day 20)
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

# KEY CONCEPT: tkinter event loop keeps window responsive to user interactions
window.mainloop()