import tkinter
import math

# =================================================================
# CONFIGURATION CONSTANTS
# =================================================================
# Hex color codes for UI theming
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# Pomodoro timings (in minutes)
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# =================================================================
# GLOBAL STATE (Track across function calls)
# =================================================================
# Counts number of sessions completed (determines work vs break)
reps = 0
# Stores scheduled timer callback ID (needed to cancel timer)
timer = None 

# =================================================================
# TIMER RESET - Reset all state
# =================================================================
def reset_timer():
    # KEY CONCEPT: Cancel scheduled timer callback to stop countdown
    # after_cancel() prevents count_down() from being called again
    window.after_cancel(timer)

    # Reset all UI elements to initial state
    timer_lable.config(text="Timer")
    check_lable.config(text="")  # Clear checkmarks
    canvas.itemconfig(timer_text, text="00:00")

    # PATTERN: Use global keyword to modify global variable
    # Without 'global', reps = 0 creates a local variable instead
    global reps
    reps = 0



# =================================================================
# TIMER LOGIC - Determine work vs break based on Pomodoro cycle
# =================================================================
def start_timer():
    global reps
    # Increment session counter
    reps += 1

    # Convert minutes to seconds for countdown
    work_sec = WORK_MIN * 60           # 1500 seconds
    short_break_sec = SHORT_BREAK_MIN * 60  # 300 seconds
    long_break_sec = LONG_BREAK_MIN * 60    # 1200 seconds

    # PATTERN: Pomodoro cycle logic using modulo operator
    # Rep 1: Work, Rep 2: Short break, Rep 3: Work, Rep 4: Short break, ...
    # Rep 8: Long break (20 min instead of 5 min), then repeat
    if reps % 8 == 0:
        # Every 8th rep: long break (after 4 complete work cycles)
        count_down(long_break_sec)
        timer_lable.config(text="Break", bg=YELLOW, fg=RED, font=(FONT_NAME, 50))
    elif reps % 2 == 0:
        # Every even rep: short break (between work sessions)
        count_down(short_break_sec)
        timer_lable.config(text="Break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 50))
    else:
        # Odd reps: work/study session
        count_down(work_sec)
        timer_lable.config(text="Study", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
    

# =================================================================
# COUNTDOWN MECHANISM - Recursively count down, update display
# =================================================================
def count_down(count):
    # Convert remaining seconds to MM:SS format
    count_min = math.floor(count / 60)  # Integer division
    count_sec = count % 60              # Remainder after dividing by 60

    # Pad seconds with leading zero if needed (5 → "05")
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # Update canvas text (not Label)
    # KEY CONCEPT: canvas.itemconfig() updates existing canvas items
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        # Schedule next countdown call in 1000ms (1 second)
        # PATTERN: window.after(delay_ms, callback_function, args)
        # KEY CONCEPT: This runs in background; GUI remains responsive
        # DO NOT use time.sleep() - blocks entire GUI
        global timer
        # timer stores callback ID so reset_timer() can cancel it
        timer = window.after(1000, count_down, count - 1)
    else:
        # Timer finished - start next phase
        start_timer()

        # Update checkmark display (visual progress tracker)
        mark = ""
        # Each completed work session = 1 study phase + 1 break phase
        # So 2 reps = 1 work session
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            # Add checkmark for each completed work session
            mark += "✔"
        check_lable.config(text=mark)
        



# =================================================================
# UI SETUP - Create window and widgets
# =================================================================
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# PATTERN: Canvas widget allows custom graphics and text overlay
# Can combine image + text in single widget (better than multiple Labels)
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# Load tomato image for visual branding
tomato_image = tkinter.PhotoImage(file="./tomato.png")
# Create image at coordinates (100, 112) - center of canvas
canvas.create_image(100, 112, image=tomato_image)

# Add text on canvas - store returned ID to update later
# canvas.itemconfig(timer_text, text="...") updates this text
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Title label - changes between "Timer", "Study", "Break"
timer_lable = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
timer_lable.grid(column=1, row=0)

# Checkmark label - displays ✔ marks for completed sessions
check_lable = tkinter.Label(fg=GREEN, bg=YELLOW)
check_lable.grid(column=1, row=3)

# Start button - calls start_timer() callback
start_button = tkinter.Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

# Reset button - calls reset_timer() callback
reset_button = tkinter.Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)


# CRITICAL: Keep window open, listening for events
window.mainloop()