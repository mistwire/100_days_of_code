# PATTERN: Simple data model (similar to MenuItem in Day 16). Encapsulates a single question.
# Compare with Day 15's nested dict: instead of question_data[i]["text"], here: question.text
class Question():
    def __init__(self, q_text, q_answer) -> None:
        # KEY CONCEPT: Instance attributes for question content.
        # These are set once during construction and read later by QuizBrain.
        self.text = q_text
        self.answer = q_answer

