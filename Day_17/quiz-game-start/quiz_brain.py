# PATTERN: Quiz state machine. Manages question progression, scoring, and user interaction.
class QuizBrain:

    def __init__(self, question_list) -> None:
        # KEY CONCEPT: State tracking for quiz progression.
        self.question_list = question_list
        self.question_number = 0  # 0-indexed internal counter
        self.score = 0  # Correct answer count

    def next_question(self):
        # PATTERN: Question-answer cycle. Get current, advance counter, display with updated number, validate.
        # CRITICAL: Fetch current_question BEFORE incrementing question_number.
        current_question = self.question_list[self.question_number]
        self.question_number += 1  # Advance BEFORE displaying (so questions are labeled Q.1, Q.2, not Q.0, Q.1)
        # Display uses incremented question_number, so user sees "Q.1", "Q.2", etc.
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        # PATTERN: Loop condition. Compare internal counter with list length.
        # Simplified: could be "return len(self.question_list) > self.question_number"
        if len(self.question_list) > self.question_number:
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        # KEY CONCEPT: Case-insensitive comparison. User might type "true" vs. "True" from API.
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1  # Increment score on correct answer
        else:
            print("That's wrong.")
        # Feedback: show correct answer and running score (uses question_number, which is now incremented)
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


