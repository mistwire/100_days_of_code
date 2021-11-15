import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="Label Here")
my_label.pack()


















# need to keep window on screen (has to be at the very end)
window.mainloop()
