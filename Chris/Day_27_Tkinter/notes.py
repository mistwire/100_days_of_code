import tkinter

window = tkinter.Tk()
# to add title to window:
window.title("My First GUI Program")
# to change default size
window.minsize(width=500, height=300)

# Label is a **kwargs entry:
my_label = tkinter.Label(text="Label Here", font=("Arial", 24, "bold"))
# need to specify how label gets displayed before it will show:
my_label.pack(expand=True)  # <-- will center the label - https://docs.python.org/3/library/tkinter.html#the-packer

# use mainloop to keep window on screen (has to be at the end)
window.mainloop()


def add(*args):
    for i in args:
        print(i)
