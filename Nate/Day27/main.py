from tkinter import *


def calculate():
    result = float(miles_input.get()) * 1.609
    km_output.config(text=result)


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=50)
window.config(padx=10, pady=10)
text_label_1 = Label(text="is equal to")
text_label_1.grid(row=1, column=0)

miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(row=0, column=1)

km_output = Label(text="0")
km_output.grid(row=1, column=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)


window.mainloop()

