import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # List of symbols:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # number of random symbols to use:
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # List comprehensions to make randomized password
    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    # Final shuffle of appended lists:
    random.shuffle(password_list)

    password = "".join(password_list)

    # Clear entry box:
    password_entry.delete(0, 'end')

    # Add newly created password to entry box & add to clipboard
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# take website, email, & password entry & save it into data.txt


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # Create new dict populated with above info:
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Don't leave empty fields")
    else:
        try:
            with open("data.json", mode="r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", mode="w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as f:
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
gui = tkinter.Tk()
gui.title("Password Manager")
gui.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
lock_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = tkinter.Entry(width=45)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = tkinter.Entry(width=45)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'fakename@email.com')
password_entry = tkinter.Entry(width=27)
password_entry.grid(column=1, row=3)

# Buttons
gen_password = tkinter.Button(text="Generate Password", command=generate_password)
gen_password.grid(column=2, row=3)
add_button = tkinter.Button(text="Add", width=38, command=save)
add_button.grid(column=1, row=4, columnspan=2)

gui.mainloop()
