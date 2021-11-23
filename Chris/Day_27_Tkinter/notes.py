import tkinter

window = tkinter.Tk()
# to add title to window:
window.title("My First GUI Program")
# to change default size
window.minsize(width=500, height=300)

# Label is a **kwargs entry:
my_label = tkinter.Label(text="Label Here", font=("Arial", 24, "bold"))
# need to specify how label gets displayed before it will show:
my_label.pack()  # <-- will center the label - https://docs.python.org/3/library/tkinter.html#the-packer
my_label["text"] = "New Text"  # Can change like a dict entry
my_label.config(text="New Text using config")  # Or via config entry

# Button

def button_clicked():
    print("I got clicked")

def button_clicked_2():
    my_label["text"] = line_input.get()


button = tkinter.Button(text="Click Me", command=button_clicked_2)
button.pack()

# Entry (basically an input) - https://tcl.tk/man/tcl8.6/TkCmd/entry.htm
line_input = tkinter.Entry(width=10)
line_input.pack()


# Challenge - make button click change label text

# Challenge - make the Entry string show up as the label when you click the button


# use mainloop to keep window on screen (has to be at the end)
window.mainloop()


def add(*args):
    for i in args:
        print(i)
