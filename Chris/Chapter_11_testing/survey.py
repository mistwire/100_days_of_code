class AnonymousSurvey:
    """Store a question, and prepare to store responses."""
    def __init__(self, question) -> None:
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey"""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given"""
        print("Surevey results:")
        for response in self.responses:
            print(f"- {response}")


