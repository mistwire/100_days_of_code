import tkinter 

window = tkinter.Tk() 
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_lable = tkinter.Label(text="I am a lable", font=("Arial", 24, "bold"))
# my_lable.pack() # pack places and centers the lable (https://docs.python.org/3/library/tkinter.html#the-packer)
my_lable.grid(column=1, row=0)

my_lable.config(text="New Text")

# Button

def button_clicked():
    print("I got clicked😏")
    my_lable.config(text="I got clicked😏")


def button_clicked2():
    my_lable.config(text=input.get())

button = tkinter.Button(text="Click Me!", command=button_clicked)
button.grid(column=0, row=1)

button2 = tkinter.Button(text="Click Me 2nd!", command=button_clicked2)
button2.grid(column=0, row=2)

# Input 

input = tkinter.Entry(width=10)
input.grid(column=3, row=3)











# This needs to be at the end to keep the window open until done:
window.mainloop() 