# Day 34: Quiz Brain GUI -- Integrating APIs into a Tkinter GUI

## What You Learned
You combined API data fetching (from Open Trivia DB) with a Tkinter GUI to build an interactive quiz application. This demonstrates the pattern of building modular, object-oriented code where one class handles the quiz logic, another manages UI, and a third owns the question data.

---

## Key Concepts

### 1. Fetching Dynamic Data from an API
Instead of hardcoding questions, the Open Trivia DB API provides unlimited question data:

```python
import requests

parameters = {
    "amount": 10,
    "type": "boolean",  # Only True/False questions
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()['results']  # Extract 'results' array
```

**Why**: APIs provide fresh, dynamic content without manual data maintenance. Parameters filter by difficulty, category, and type.

### 2. HTML Entity Decoding
The Open Trivia DB returns HTML-encoded special characters:

```python
import html

q_text = html.unescape(self.current_question.text)
# "Which planet is the largest?" becomes "Which planet is the largest?"
# "&quot;Question&quot;" becomes "\"Question\""
```

**Why**: HTML entities protect special characters in JSON; decoding makes text human-readable.

### 3. Model-View-Controller (MVC) Architecture
The quiz is split into three classes:
- **Question (Model)**: Holds question text and answer—pure data
- **QuizBrain (Controller)**: Manages quiz logic (scoring, question progression, validation)
- **QuizInterface (View)**: Handles GUI rendering and user interaction

```python
# main.py orchestrates all three
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
```

**Why**: Separation of concerns makes code testable, reusable, and maintainable. UI can change without touching quiz logic.

### 4. State Management in the Controller
QuizBrain maintains the quiz state:

```python
def __init__(self, q_list):
    self.question_number = 0  # Track progress
    self.score = 0            # Track correct answers
    self.question_list = q_list
    self.current_question = None

def still_has_questions(self):
    return self.question_number < len(self.question_list)
```

**Why**: Centralizing state logic prevents bugs and makes state transitions predictable.

### 5. Type Hints for Clarity
Function signatures specify expected types (Python 3.5+):

```python
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

def send_true(self) -> None:
    is_right = self.quiz.check_answer("True")
    self.give_feedback(is_right)
```

**Why**: Type hints document intent, catch errors in IDEs, and make code self-documenting (no need for comments like "expects a QuizBrain").

### 6. Tkinter Canvas for Dynamic Content
Canvas updates text without recreating widgets:

```python
self.question_text = self.canvas.create_text(
    150, 125,
    width=270,
    text="Question",
    fill=THEME_COLOR,
    font=("Arial", 20, "italic")
)

# Later, update the text without redrawing the canvas
self.canvas.itemconfig(self.question_text, text=q_text)
```

**Why**: Canvas is lightweight and flexible; `itemconfig()` updates existing items efficiently.

### 7. Timed Feedback with `.after()`
Show visual feedback (color change) then proceed after a delay:

```python
def give_feedback(self, is_right):
    if is_right:
        self.canvas.config(bg="green")
    else:
        self.canvas.config(bg="red")
    # Schedule next question after 1000 ms (1 second)
    self.window.after(1000, self.get_next_question)
```

**Why**: Delays allow users to see if they're correct before the next question appears; creates a smooth UX.

### 8. Disabling Widgets on Quiz End
When all questions are answered, disable buttons:

```python
if not self.quiz.still_has_questions():
    self.canvas.itemconfig(self.question_text, text="You're done!")
    self.true_button.config(state="disabled")
    self.false_button.config(state="disabled")
```

**Why**: Prevents users from clicking buttons with no effect; signals quiz completion.

---

## Common Pitfalls
- **Not decoding HTML entities**: Quotes, ampersands, and accents appear as `&quot;` or `&amp;` instead of readable characters.
- **Forgetting to parse the 'results' key**: The API response is `{"response_code": 0, "results": [...]}`, not the array directly.
- **Mixing model and view logic**: Putting quiz scoring in the UI class makes it hard to test and reuse.
- **Not storing `current_question`**: Checking answers requires knowing which question the user just saw.
- **Hardcoding question data**: Makes it impossible to refresh or change difficulty dynamically.

---

## Connections to Other Days

| Day | Connection |
|-----|-----------|
| **Day 17 (Quiz Game)** | Text-based quiz logic; this is the GUI evolution of that concept |
| **Day 27 (Tkinter)** | GUI framework; buttons, canvas, and event handling |
| **Day 28 (Pomodoro)** | `.after()` for delayed actions after timer completion |
| **Day 33 (ISS Tracker)** | API fetching pattern (requests, JSON parsing, error handling) |
| **Day 35 (Weather API)** | Environment variables for API keys; multiple endpoint patterns |
| **Day 36 (Stock Tracker)** | Multi-API integration and data combination |

---

## Before You Move On

Make sure you can:
- [ ] Fetch data from a public API and parse the JSON response
- [ ] Filter API results using query parameters (amount, type, difficulty)
- [ ] Decode HTML entities from API responses using the `html` module
- [ ] Organize code into Model, View, and Controller classes
- [ ] Use type hints in function signatures
- [ ] Update Tkinter canvas text dynamically with `itemconfig()`
- [ ] Schedule delayed actions with `window.after()`
- [ ] Disable/enable widgets based on application state
- [ ] Pass quiz results to the view for display (score out of total)

---

## Practice Prompt
Build a **Category-Filtered Quiz**: Extend this quiz to let the user select a category (General Knowledge, Science, History, etc.) from a dropdown before starting. The app should fetch questions for that category via the API. Add a difficulty selector (Easy, Medium, Hard) as well. Bonus: Save high scores to a file and display a leaderboard at startup.
