from question_model import Question
from data import question_data  # Fetched from Open Trivia DB API
from quiz_brain import QuizBrain
from ui import QuizInterface

# PATTERN: Model-View-Controller (MVC) architecture
# 1. Convert raw API data into Question objects (Model)
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# 2. Create controller (handles quiz logic)
quiz = QuizBrain(question_bank)
# 3. Create view (handles GUI and user interaction)
# Passing quiz to UI so UI can query state and call methods
quiz_ui = QuizInterface(quiz)

# NOTE: In text-based version, this loop would be here:
# while quiz.still_has_questions():
#     quiz.next_question()
# But Tkinter runs its own event loop (window.mainloop()),
# so questions are driven by button clicks, not a loop

# Print final score after GUI closes
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
