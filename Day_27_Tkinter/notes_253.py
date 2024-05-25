import tkinter


def button_clicked():
    print("I got clicked")
    new_text = line_input.get()
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# Add padding to edges of window to move widgets in a bit:
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="Label Here", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
# add padding to a specific widget:
my_label.config(padx=20, pady=20)


# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# NewButton
button2 = tkinter.Button(text="Button 2")
button2.grid(column=2, row=0)

# Entry (basically an input) - https://tcl.tk/man/tcl8.6/TkCmd/entry.htm
line_input = tkinter.Entry(width=10)
line_input.grid(column=3, row=2)


# tkinter layout managers - pack(), place(), & grid()
# with pack it's hard to be precise with positioning
# place - all about precise positioning with an x & y value
# (0, 0) = top left corner
# e.g. my_label.place(x=0, y=0)
# place can be TOO specific - that's where we get grid()
# divide program into any # of columns and rows
# e.g. my_label.grid(column=0, row=0) = top left corner
# start at top left, for next widgets defining positions
#   col1/row0   row0    row0    row0/
#   col1/row1   col2    col3    colN
#   col1/row2   col2    col3    colN
#   col1/row3   col2    col3    colN/rowN
#
# WARNING - you can't mix grid() and pack() - it will error out

# Challenge - create new app with grid() layout for label(0, 0) Button(1, 1), NewButton(3, 0), Entry(4, 3)

# to add padding around elements



# use mainloop to keep window on screen (has to be at the end)
window.mainloop()
