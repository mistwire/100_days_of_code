import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Images
        true_image = tkinter.PhotoImage(file="images/true.png")
        false_image = tkinter.PhotoImage(file="images/false.png")

        # Label
        self.score_label = tkinter.Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        # Canvas
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

        # Buttons
        self.true_button = tkinter.Button(image=true_image, highlightthickness=0, command=self.send_true)
        self.true_button.grid(column=0, row=2)
        self.false_button = tkinter.Button(image=false_image, highlightthickness=0, command=self.send_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You're done!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def send_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def send_false(self):
        # Does the same thing as the line above but in 1 line:
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)




