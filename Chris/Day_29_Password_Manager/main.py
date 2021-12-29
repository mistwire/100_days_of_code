import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
# take website, email, & password entry & save it into data.txt





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
email_entry.insert(0, 'chrisfwilliams@gmail.com')
password_entry = tkinter.Entry(width=27)
password_entry.grid(column=1, row=3)

# Buttons
gen_password = tkinter.Button(text="Generate Password")
gen_password.grid(column=2, row=3)
add_button = tkinter.Button(text="Add", width=38)
add_button.grid(column=1, row=4, columnspan=2)






gui.mainloop()

