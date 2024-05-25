import tkinter

import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    gui.after_cancel(timer)
    # timer text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # reset checkmarks
    check_marks.config(text="")
    # label back to "Timer"
    timer_label.config(text="Timer", fg=GREEN)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global timer_label
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    gui.attributes("-topmost", 1)
    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    gui.attributes("-topmost", 0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = gui.after(1000, count_down, count - 1)  # https://tcl.tk/man/tcl8.6/TclCmd/after.htm
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

gui = tkinter.Tk()
gui.title("Pomodoro Timer")
gui.config(padx=100, pady=50)
gui.config(bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36, "bold"))
timer_label.grid(column=1, row=0)

check_marks = tkinter.Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

gui.mainloop()
