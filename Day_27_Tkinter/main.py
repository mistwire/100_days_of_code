import tkinter 

window = tkinter.Tk() 
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Widgets

def miles_to_km():
    miles = float(miles_input.get()) 
    km = miles * 1.609
    answer_lable.config(text=f"{km}")

miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1, row=0)

miles_lable = tkinter.Label(text="Miles")
miles_lable.grid(column=2, row=0)

km_lable = tkinter.Label(text="Km")
km_lable.grid(column=2, row=1)

is_equal_lable = tkinter.Label(text="is equal to")
is_equal_lable.grid(column=0, row=1)

answer_lable = tkinter.Label(text="0")
answer_lable.grid(column=1, row=1)


button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)



window.mainloop() 