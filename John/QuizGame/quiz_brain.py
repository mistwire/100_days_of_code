#TODO: 1: asking the questions
#TODO: 2: checking if the answer was correct
#TODO: 3: checking if we're at the end of the quiz

#EXAMPLE: Format of question presentation:
# Q.1: A slug's blood is green. (True/False)?:
class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.questions_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.text}. (True/False)? ')
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Sorry! Not correct")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

