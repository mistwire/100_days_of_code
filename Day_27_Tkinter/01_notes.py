import tkinter 

window = tkinter.Tk() 
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_lable = tkinter.Label(text="I am a lable", font=("Arial", 24, "bold"))
my_lable.pack() # pack places and centers the lable (https://docs.python.org/3/library/tkinter.html#the-packer)

















# This needs to be at the end to keep the window open until done:
window.mainloop() 