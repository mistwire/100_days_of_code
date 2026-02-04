# Day 17: Quiz Game with API Data

## What You Learned
This project demonstrates **API data integration** with a class-based quiz engine. You learn how to fetch questions from an external API (Open Trivia Database), parse JSON responses, and build a quiz system with score tracking. This bridges the gap between local data (Day 15-16) and real-world data sources.

---

## Key Concepts
### 1. External API Integration
The quiz fetches data from OpenTDB (Open Trivia Database):
```python
# https://opentdb.com/
# The comment indicates the data source (normally retrieved via HTTP requests).
# In this version, data is pre-downloaded as question_data list.
```

In production, you'd use the `requests` library:
```python
import requests
response = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')
question_data = response.json()['results']
```

The curriculum simplifies this by providing pre-made `data.py`.

### 2. Data Class (Simple Model)
`Question` is a minimal data container:

```python
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```

Similar to Day 16's `MenuItem`, this encapsulates a single question. Compared to Day 15's nested dict approach, this is more explicit.

### 3. Stateful Quiz Engine (QuizBrain)
`QuizBrain` manages the quiz state and progression:

```python
class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
```

This tracks:
- **question_number**: Progress through the quiz (0-indexed, incremented in `next_question()`)
- **score**: Count of correct answers
- **question_list**: Reference to the bank of questions

### 4. Question-Answer Cycle
The quiz loop follows a clear pattern:

```python
while quiz.still_has_questions():
    quiz.next_question()  # Display question, get answer, check it
```

Inside `next_question()`:
```python
def next_question(self):
    current_question = self.question_list[self.question_number]  # Access current
    self.question_number += 1  # Advance BEFORE asking (so Q.1, Q.2, etc.)
    user_answer = input(f"Q.{self.question_number}: ...")  # Display updated counter
    self.check_answer(user_answer, current_question.answer)  # Validate
```

**Important detail**: `question_number` is incremented BEFORE displaying, so questions are labeled Q.1, Q.2, not Q.0, Q.1.

### 5. Answer Validation with Case-Insensitivity
```python
def check_answer(self, user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
        # Case-insensitive comparison (user might type "true" or "True")
        self.score += 1
```

This is more forgiving than exact matching and matches real-world requirements.

### 6. JSON Data Structure (Trivia Format)
From `data.py`:
```python
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    # ...
]
```

Each question is a dict with "text" (the question) and "answer" (the correct answer as a string). This mirrors typical API responses.

### 7. Bootstrapping Objects from Data
The main entry point constructs the quiz:

```python
question_bank = []
for question in question_data:
    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
```

This transforms raw data (list of dicts) into object instances. A common pattern when consuming APIs.

---

## Common Pitfalls
- **Off-by-one in question numbering**: Incrementing `question_number` BEFORE asking displays Q.1-Q.13 correctly (not Q.0-Q.12 or Q.1-Q.14).
- **Forgetting the `.lower()` call**: User enters "true" but API provides "True"—comparison fails without normalization.
- **Accessing `question_list[question_number]` AFTER incrementing**: Must fetch the current question before advancing the counter, otherwise you'd display the next question.
- **Not breaking when a question isn't found**: The loop continues even if a question index is out of bounds (depending on list length).
- **None check for API response**: In a real API call, responses can be `None` or malformed. This code assumes valid data.

---

## Connections to Other Days
| Day | Connection |
|-----|-----------|
| **Day 1** | OOP fundamentals (classes, state, methods) |
| **Day 9** | Dictionary iteration (`for question in question_data`) |
| **Day 14** | Game data structures; here data comes from API instead of local file |
| **Day 15-16** | State tracking and validation patterns applied to quiz |
| **Day 18-19** | Turtle graphics projects also use state machines and event loops |
| **Day 27** | Tkinter quiz UI would replace the terminal interface here |

---

## Before You Move On
Make sure you can:
- [ ] Explain the difference between `question_number` and the actual position in `question_list`
- [ ] Understand why `question_number` increments BEFORE using it in the display
- [ ] Trace through a full quiz: data loading → object creation → loop → scoring
- [ ] Explain how JSON data (dicts) maps to Python objects
- [ ] Understand case-insensitive comparison and why it matters
- [ ] Predict what would happen if you removed the `.lower()` call from `check_answer()`

---

## Practice Prompt
**Mini-Project: Quiz Game with Multiple Categories**
Extend Day 17's quiz system:

1. Modify `Question` to include a `category` attribute:
   ```python
   class Question:
       def __init__(self, q_text, q_answer, category):
           self.text = q_text
           self.answer = q_answer
           self.category = category
   ```

2. Update `data.py` to include category info:
   ```python
   question_data = [
       {"text": "...", "answer": "True", "category": "Science"},
       {"text": "...", "answer": "False", "category": "History"},
   ]
   ```

3. Extend `QuizBrain`:
   - Add `score_by_category` dict to track scores per category
   - Modify `check_answer()` to update category scores
   - Add `category_report()` method showing performance by category

4. In `main.py`, allow the user to:
   - Choose a category to quiz on (filter `question_data` before building `question_bank`)
   - See their score and category breakdown at the end

5. **Bonus**: Add difficulty levels (Easy/Medium/Hard) to questions. Track score by both category AND difficulty.

**Challenge Extension**: What would break if the API returned `"answer": "true"` (lowercase) but data files used uppercase? How does your code handle this?
