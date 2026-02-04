import tkinter

# KEY CONCEPT: Create root window object
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
# PATTERN: Add padding around window content for better appearance
window.config(padx=20, pady=20)

# =================================================================
# CALLBACK FUNCTION (runs when button is clicked)
# =================================================================
def miles_to_km():
    # KEY CONCEPT: Entry.get() returns string; convert to float for math
    miles = float(miles_input.get())
    km = miles * 1.609
    # PATTERN: Modify existing widget with .config()
    answer_lable.config(text=f"{km}")


# =================================================================
# WIDGETS - Created but not yet visible
# =================================================================

# Input field for miles
# PATTERN: Create widget → grid it
miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1, row=0)

# Label: "Miles" (static text)
miles_lable = tkinter.Label(text="Miles")
miles_lable.grid(column=2, row=0)

# Label: "Km" (static text)
km_lable = tkinter.Label(text="Km")
km_lable.grid(column=2, row=1)

# Label: "is equal to" (static text)
is_equal_lable = tkinter.Label(text="is equal to")
is_equal_lable.grid(column=0, row=1)

# Label: displays answer (will be updated by callback)
# PATTERN: Initialize with default value, then update with .config()
answer_lable = tkinter.Label(text="0")
answer_lable.grid(column=1, row=1)


# Button: triggers miles_to_km callback
# IMPORTANT: command=miles_to_km (no parentheses!)
# command=miles_to_km() would call function immediately, not on click
button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


# CRITICAL: Keep window open and listening for events
# Without this, window closes immediately after creating widgets
window.mainloop() 