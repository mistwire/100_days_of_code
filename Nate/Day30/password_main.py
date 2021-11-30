from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json


def password_gen():
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(16))
    password_input.delete(0, END)
    password_input.insert(0, password)


def add_password():
    website = website_input.get()
    user_email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": user_email,
            "password": password,
        }
    }

    if not password or not website:
        messagebox.showwarning(title="Missing Information", message="You left required fields blank, please check.")
    else:
        pyperclip.copy(password)
        website_input.delete(0, END)
        password_input.delete(0, END)
        try:
            with open("passwords.json", "r") as f:
                data = json.load(f)
                data.update(new_data)
        except FileNotFoundError:
            with open("passwords.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            with open("passwords.json", "w") as f:
                json.dump(data, f, indent=4)


def search():
    website = website_input.get()

    try:
        with open("passwords.json", "r") as f:
            data = json.load(f)
            for entry in data:
                if entry == website:
                    email = data[entry]["email"]
                    password = data[entry]["password"]
                    pyperclip.copy(password)
                    messagebox.showinfo(title=entry, message=f"Email: {email}\nPassword: {password}\nPassword copied"
                                                             f" to clipboard")
    except FileNotFoundError:
        pass

# ---------------------------- UI  ------------------------------- #


window = Tk()
window.title("Password Manager")
window.minsize(width=240, height=240)
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(105,110, image=bg_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky=E)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky=E)
password_label = Label(text="password:")
password_label.grid(row=3, column=0, sticky=E)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky=W, padx=20)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky=W, padx=20)
email_input.insert(END, "email@email.com")
password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky=W, padx=20)

search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2)
generate_button = Button(text="Generate Password", command=password_gen)
generate_button.grid(row=3, column=2, sticky=W)
add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=4, column=1, columnspan=2, sticky=W, padx=20)



window.mainloop()