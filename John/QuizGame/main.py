from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
#print(question_data)

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))


quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print(f"You've finished the quiz!\nYour final score was: {quiz.score}/{len(question_bank)}")