import html  # KEY CONCEPT: Decode HTML entities from API response


class QuizBrain:
    """Controller for quiz logic (Model in MVC).

    Manages quiz state: progress, scoring, and answer validation.
    Does NOT handle UI or data fetching—those are separate concerns.
    """

    def __init__(self, q_list):
        self.question_number = 0     # 0-based index of current question
        self.score = 0               # Count of correct answers
        self.question_list = q_list  # List of Question objects
        self.current_question = None # Pointer to current question (set by next_question())

    def still_has_questions(self):
        """Check if there are more questions to ask."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Move to next question and return formatted text for display."""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # KEY CONCEPT: Open Trivia DB returns HTML-encoded text (&quot;, &amp;, &nbsp;)
        # html.unescape() converts these to readable characters
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"
        # NOTE: In text-based version, this would also prompt for input:
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer)
        # But GUI-based version separates answer input from question display

    def check_answer(self, user_answer):
        """Validate user answer and update score.

        Args:
            user_answer: "True" or "False" string from user

        Returns:
            bool: True if answer is correct, False otherwise
        """
        correct_answer = self.current_question.answer
        # Case-insensitive comparison (API might return "True" or "true")
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
