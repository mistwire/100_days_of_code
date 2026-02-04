# Day 28: Pomodoro Timer - Advanced Tkinter and Time Management

## What You Learned
Advanced Tkinter features: Canvas widget for custom graphics, timer callbacks with `after()`, global state management, and implementing the Pomodoro productivity technique (25-min focus / 5-min break cycles).

---

## Key Concepts

### 1. Tkinter Canvas Widget - Custom Graphics
Draw shapes and images directly on canvas:

```python
# Create canvas
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# Load and display image
tomato_image = tkinter.PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_image)

# Add text on canvas (not Label widget)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# Update canvas text later
canvas.itemconfig(timer_text, text="05:00")

# Grid canvas like any other widget
canvas.grid(column=1, row=1)
```

**Why canvas?** Allows custom layouts, overlays images with text, more control than Labels.

### 2. Timer Mechanism with window.after()
Implement countdown without blocking GUI:

```python
# Global variable to store timer callback ID (so we can cancel later)
timer = None

def count_down(count):
    # Format minutes and seconds
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # Pad single digits with 0

    # Update display
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        # Schedule next countdown call in 1000ms (1 second)
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # Timer finished, start next phase
        start_timer()
```

**Pattern:** `window.after(ms, function, args)` schedules function to run after delay.

**Why not time.sleep()?** Blocks entire GUI; user can't interact. `after()` runs in background.

### 3. Pomodoro Cycle Logic
Alternate between work and break sessions:

```python
# Global state
reps = 0  # Counts number of sessions

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60      # 25 * 60 = 1500 seconds
    short_break_sec = SHORT_BREAK_MIN * 60  # 5 * 60 = 300 seconds
    long_break_sec = LONG_BREAK_MIN * 60    # 20 * 60 = 1200 seconds

    # Pomodoro cycle:
    # Rep 1: Work (25 min)
    # Rep 2: Short break (5 min)
    # Rep 3: Work (25 min)
    # Rep 4: Short break (5 min)
    # ...
    # Rep 8: Long break (20 min)
    # Then repeat

    if reps % 8 == 0:
        # Every 8th rep: long break
        count_down(long_break_sec)
        timer_lable.config(text="Break", bg=YELLOW, fg=RED, font=(FONT_NAME, 50))
    elif reps % 2 == 0:
        # Every even rep (except 8): short break
        count_down(short_break_sec)
        timer_lable.config(text="Break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 50))
    else:
        # Odd reps: work
        count_down(work_sec)
        timer_lable.config(text="Study", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
```

### 4. Reset Mechanism
Cancel running timer and reset state:

```python
def reset_timer():
    # Cancel the scheduled timer callback
    window.after_cancel(timer)

    # Reset display
    timer_lable.config(text="Timer")
    check_lable.config(text="")
    canvas.itemconfig(timer_text, text="00:00")

    # Reset state
    global reps
    reps = 0
```

### 5. Session Tracking with Checkmarks
Visual feedback for completed work sessions:

```python
# In count_down(), when timer reaches zero:
else:
    start_timer()
    mark = ""
    # Calculate completed work sessions (each session = 1 study + 1 break)
    work_sessions = math.floor(reps / 2)
    for i in range(work_sessions):
        mark += "✔"  # Add checkmark for each completed session
    check_lable.config(text=mark)
```

### 6. Global Variable Management
Use `global` keyword to modify globals from within functions:

```python
timer = None  # Global variable to store timer callback ID

def some_function():
    global timer  # Declare we're modifying the global timer
    timer = window.after(1000, count_down, 1)  # Schedule callback

def reset_timer():
    global reps  # Declare we're modifying the global reps
    reps = 0  # Reset
    window.after_cancel(timer)  # Cancel scheduled timer
```

---

## Common Pitfalls
- **No `global` declaration**: Changes to globals inside functions create local variables instead
- **`timer = None` inside count_down()**: Create local variable instead of assigning to global
- **Using time.sleep()**: Blocks GUI; user can't click buttons while timer runs
- **Image file not found**: Check file path (./tomato.png relative to script location)
- **Timer doesn't stop**: Forgetting to call `window.after_cancel(timer)` leaves callbacks scheduled
- **`.item_config` vs `.itemconfig`**: Correct method is `.itemconfig()` (no underscore)
- **PhotoImage reference lost**: Must keep reference: `self.image = PhotoImage(...)` or it's garbage collected

---

## Connections to Other Days
| Day | Connection |
|-----|-----------|
| **Day 1** | Classes and global state management concepts |
| **Day 8** | Functions and callbacks (button clicks call start_timer/reset_timer) |
| **Day 12** | Global variables: reps, timer, workspace state |
| **Day 27** | Tkinter basics: Labels, Buttons, grid layout, window.mainloop() |
| **Day 34** | Combine OOP with this: Create Pomodoro class instead of global variables |
| **Day 35+** | APIs: Could store pomodoro sessions in database or cloud storage |

---

## Before You Move On
Make sure you can:
- [ ] Explain how `window.after()` works vs `time.sleep()`
- [ ] Trace through one complete Pomodoro cycle (rep 1-8)
- [ ] Understand why `global` keyword is needed
- [ ] Draw text and images on Canvas
- [ ] Cancel scheduled callbacks with `after_cancel()`
- [ ] Format time display: MM:SS with leading zeros
- [ ] Explain modulo operators in cycle logic (% 8, % 2)

---

## Practice Prompt
**Challenge: Enhanced Pomodoro Timer**
1. Add session type labels (Work/Short Break/Long Break)
2. Add sound notifications when timer ends (Day 18+ techniques)
3. Persist session history:
   - Save timestamps of completed work sessions to file (Day 2)
   - Display total work time for today
   - Show longest focus streak
4. Add pause/resume buttons (not just stop)
5. Add difficulty selector:
   - Beginner: 15 min work, 3 min break
   - Intermediate: 25 min work, 5 min break (current)
   - Advanced: 45 min work, 15 min break
6. Display current focus streak (how many consecutive work sessions)
7. Optional: Add background music that plays during work sessions

This combines Tkinter (Day 27), timers (Day 28), file I/O (Day 2), and OOP design patterns.
