from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
intervals = 0
check_mark = "✔"
timer = None
is_running = False


def raise_above_all(win):
    win.attributes('-topmost', 1)
    win.attributes('-topmost', 0)

# ---------------------------- TIMER RESET ------------------------------- #


def timer_reset():
    global is_running
    global intervals
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_count_label.config(text="")
    intervals = 0
    is_running = False


# ---------------------------- TIMER MECHANISM ------------------------------- #

def timer_start():
    global intervals
    global check_mark
    global is_running
    intervals += 1

    if not is_running:
        is_running = True
        if intervals == 8:
            title_label.config(text="Long Break", fg=RED)
            count_down(LONG_BREAK_MIN * 60)
            intervals = 0
        elif intervals % 2 == 0:
            title_label.config(text="Break", fg=PINK)
            count_down(SHORT_BREAK_MIN * 60)
        else:
            title_label.config(text="Work", fg=GREEN)
            count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global intervals

    minutes = int(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f'0{seconds}'
    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        global is_running
        is_running = False
        check_count_label.config(text=check_mark * int(intervals / 2))
        raise_above_all(window)
        timer_start()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
title_label.grid(row=0, column=1)


start_button = Button(text="Start", command=timer_start)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", command=timer_reset)
reset_button.grid(row=2, column=2)


check_count_label = Label(bg=YELLOW, fg=GREEN)
check_count_label.grid(row=3, column=1)


canvas = Canvas(width=200, heigh=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 135, text="25:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

window.mainloop()
