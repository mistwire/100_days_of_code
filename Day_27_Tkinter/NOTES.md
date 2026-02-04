# Day 27: Tkinter - GUI Programming Fundamentals

## What You Learned
Cross-platform GUI programming: creating windows, adding widgets (Labels, Buttons, Entry fields), layout management with grid(), and event handling through callbacks. This day transitions from terminal-based programs to interactive user interfaces.

---

## Key Concepts

### 1. Window Creation and Configuration
Create a GUI window and configure its properties:

```python
import tkinter

# Create window object
window = tkinter.Tk()
window.title("My GUI Program")
window.minsize(width=500, height=300)

# Configure padding around window content
window.config(padx=20, pady=20)

# CRITICAL: Keep window open (blocks execution until window closes)
window.mainloop()
```

**Why mainloop()?** Without it, window appears and immediately closes. `mainloop()` runs forever, waiting for events.

### 2. Widget Creation and Positioning
Create widgets (UI elements) and place them using grid layout:

```python
# Create label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=0)

# Modify label after creation
my_label.config(text="New Text")

# Create button with callback function
def button_clicked():
    my_label.config(text="Button was clicked!")

button = tkinter.Button(text="Click Me!", command=button_clicked)
button.grid(column=0, row=1)

# Create entry field (text input)
input_field = tkinter.Entry(width=10)
input_field.grid(column=3, row=3)
```

**Pattern:** Create widget → Grid it (place on screen) → Optionally config/callback

### 3. Grid Layout Manager
Position widgets using row/column coordinates:

```python
# Widget at column=1, row=0 (top center)
label1.grid(column=1, row=0)

# Widget at column=0, row=1 (left middle)
label2.grid(column=0, row=1)

# Widget at column=2, row=1 (right middle)
label3.grid(column=2, row=1)

# Layout visualized:
#   Col 0    Col 1    Col 2
# [label2] [label1] [label3]  Row 1
#        [empty]   [empty]    Row 0
```

**Why grid()?** More intuitive than pack() for form-like layouts; easy to visualize.

### 4. Input and Callback Functions
Get data from Entry widgets and respond to button clicks:

```python
# Define callback function (runs when button clicked)
def miles_to_km():
    miles = float(miles_input.get())  # Get value from Entry widget
    km = miles * 1.609
    answer_label.config(text=f"{km}")

# Create Entry widget
miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1, row=0)

# Create Button with callback
button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

# Create Label to display result
answer_label = tkinter.Label(text="0")
answer_label.grid(column=1, row=1)
```

**Pattern:** Entry.get() returns string; convert with int() or float() as needed.

### 5. Multiple Widget Types (from 02_notes.py)

```python
from tkinter import *

# Text widget (multi-line)
text = Text(height=5, width=30)
text.focus()  # Set focus (cursor starts here)
text.insert(END, "Example text")
text.pack()

# Spinbox (increment/decrement number)
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_callback)
spinbox.pack()

# Scale (slider)
scale = Scale(from_=0, to=100, command=scale_callback)
scale.pack()

# Checkbutton (checkbox)
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=check_callback)
checkbutton.pack()

# Radiobutton (single choice from group)
radio_state = IntVar()
radio1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_callback)
radio2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_callback)
radio1.pack()
radio2.pack()

# Listbox (selectable list)
listbox = Listbox(height=4)
for item in ["Apple", "Pear", "Orange", "Banana"]:
    listbox.insert(END, item)
listbox.bind("<<ListboxSelect>>", listbox_callback)
listbox.pack()
```

### 6. State Variables (IntVar, StringVar, etc.)
Store and retrieve widget state:

```python
from tkinter import IntVar

# Create variable to hold checkbox state
checked_state = IntVar()  # Holds 0 (off) or 1 (on)

# Link to checkbox
checkbutton = Checkbutton(text="Is On?", variable=checked_state)

# Read current value
if checked_state.get() == 1:
    print("Checkbox is checked")
```

---

## Common Pitfalls
- **No mainloop()**: Window appears and closes immediately
- **Forgetting to grid()**: Widget created but not visible (need grid/pack/place)
- **String instead of int from Entry**: `miles_input.get()` returns string; must convert with `int()` or `float()`
- **Function called instead of referenced**: Use `command=my_function` not `command=my_function()` (no parentheses)
- **Widget destroyed after function**: If local variable, garbage collector may delete widget; store as instance variable
- **Column/row overlap**: Two widgets at same grid position; last one overwrites first

---

## Connections to Other Days
| Day | Connection |
|-----|-----------|
| **Day 1** | Classes: Widgets are objects with methods and attributes |
| **Day 4** | String formatting: Use f-strings in label text |
| **Day 8** | Functions as callbacks: Button clicks call functions |
| **Day 12** | Scope: GUI variables must persist (can't be local) |
| **Day 24-26** | File I/O and data: GUIs often read/write files and process data |
| **Day 28** | Tkinter Canvas: Draw on GUI windows |
| **Day 34** | Combined OOP + Tkinter: Scale to larger applications |

---

## Before You Move On
Make sure you can:
- [ ] Create a window and keep it open with mainloop()
- [ ] Add widgets (Label, Button, Entry) and grid them
- [ ] Create callback functions triggered by button clicks
- [ ] Get text from Entry widget with .get()
- [ ] Modify widget appearance with .config()
- [ ] Distinguish between grid() and pack() layout
- [ ] Create at least 3 different widget types

---

## Practice Prompt
**Challenge: BMI Calculator GUI**
1. Create window with title "BMI Calculator"
2. Add Entry fields for weight (kg) and height (cm)
3. Add Button "Calculate"
4. Calculate BMI: weight / (height in meters)^2
5. Display result in Label
6. Color-code result:
   - Green if BMI < 25 (healthy)
   - Yellow if 25-30 (overweight)
   - Red if > 30 (obese)
7. Add "Reset" button to clear fields
8. Add Label showing BMI category (Underweight, Normal, Overweight, Obese)

This chains Days 1 (functions), 4 (strings), 8 (callbacks), 12 (scope) with new GUI skills.
