# https://opentdb.com/
# KEY CONCEPT: Open Trivia Database API source. In this version, data is pre-downloaded.
# In a full implementation, would use: import requests; response = requests.get(url); question_data = response.json()

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# PATTERN: Data transformation. Convert raw dicts from API into Question objects.
# This is a common pattern when consuming external data sources.
question_bank = []

for question in question_data:
    # Each question dict has 'text' and 'answer' keys (from the API format)
    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)

# Create quiz engine with the processed question bank
quiz = QuizBrain(question_bank)

# PATTERN: Main loop. quiz.still_has_questions() returns True while questions remain.
# Inside next_question(), QuizBrain displays the question, collects answer, updates score.
while quiz.still_has_questions():
    quiz.next_question()

# Final summary: quiz.question_number indicates total questions asked (equals len(question_bank))
print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")

