class Question:
    """Simple data model for a quiz question (Model in MVC).

    Holds question text and the correct answer.
    No logic beyond storing data—keeps it reusable and testable.
    """

    def __init__(self, q_text, q_answer):
        self.text = q_text          # Question string (may contain HTML entities)
        self.answer = q_answer      # Correct answer ("True" or "False")
