# Mi to Km converter:
import tkinter


def button_clicked():
    print("I got clicked")
    miles = float(line_input.get())
    km = round(miles * 1.609, 2)
    converted.config(text=km)


window = tkinter.Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# Miles label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

# Km label
km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

# is equal to label
is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=10, pady=10)

# entry
line_input = tkinter.Entry(width=10)
line_input.grid(column=1, row=0)

# calculate button
button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# converted label
converted = tkinter.Label(text=0)
converted.grid(column=1, row=1)



window.mainloop()

