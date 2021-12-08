from quiz_brain import QuizBrain
from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, pady=10)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Test Question",
            font=("arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, borderwidth=0, highlightthickness=0, command=self.select_true)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, borderwidth=0, highlightthickness=0, command=self.select_false)
        self.false_button.grid(row=2, column=1, pady=50)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=self.question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End Of Quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def select_true(self):
        self.feedback(self.quiz.check_answer("True"))

    def select_false(self):
        self.feedback(self.quiz.check_answer("True"))

    def feedback(self, answer):
        if answer:
            self.canvas.configure(bg="green")
            self.window.after(1000, self.get_next_question)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.configure(bg="red")
            self.window.after(1000, self.get_next_question)

