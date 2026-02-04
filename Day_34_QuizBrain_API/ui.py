import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    """View for quiz (GUI in MVC).

    Handles all Tkinter widgets, user interactions, and visual feedback.
    Delegates quiz logic to QuizBrain; queries state and calls methods.
    """

    def __init__(self, quiz_brain: QuizBrain):
        # TYPE HINT: quiz_brain must be a QuizBrain instance (helps IDE catch errors)
        self.quiz = quiz_brain

        # PATTERN: Set up Tkinter window (see Day 27)
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Load button images
        true_image = tkinter.PhotoImage(file="images/true.png")
        false_image = tkinter.PhotoImage(file="images/false.png")

        # Score label (top-right)
        self.score_label = tkinter.Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        # Canvas for displaying questions
        # KEY CONCEPT: Canvas allows dynamic text updates without recreating widgets
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=270,
            text="Question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # True/False buttons with callback functions
        self.true_button = tkinter.Button(image=true_image, highlightthickness=0, command=self.send_true)
        self.true_button.grid(column=0, row=2)
        self.false_button = tkinter.Button(image=false_image, highlightthickness=0, command=self.send_false)
        self.false_button.grid(column=1, row=2)

        # Load first question and start event loop
        self.get_next_question()

        # PATTERN: mainloop() keeps window responsive to user interactions
        # Execution returns here only when window is closed
        self.window.mainloop()

    def get_next_question(self):
        """Update canvas with next question or show completion message."""
        self.canvas.config(bg="white")  # Reset canvas color from feedback
        if self.quiz.still_has_questions():
            # Update score display
            self.score_label.config(text=f"Score: {self.quiz.score}")
            # Get next question and update canvas text
            # KEY CONCEPT: itemconfig() updates existing canvas items without redrawing
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # Quiz is done
            self.canvas.itemconfig(self.question_text, text="You're done!")
            # PATTERN: Disable buttons to prevent further interaction
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def send_true(self):
        """Handle True button click."""
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def send_false(self):
        """Handle False button click."""
        # PATTERN: Condensed version—same as two lines in send_true()
        # Calls check_answer and passes result directly to give_feedback
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        """Show visual feedback then load next question after delay.

        Args:
            is_right: bool indicating if user's answer was correct
        """
        # Change canvas color to provide immediate feedback
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # KEY CONCEPT: window.after() schedules a callback after delay (milliseconds)
        # This allows user to see feedback before next question appears
        self.window.after(1000, self.get_next_question)  # 1000 ms = 1 second




