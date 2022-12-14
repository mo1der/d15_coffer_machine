from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

class QuizInterface:

    def button_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def button_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        # self.window.minsize(width=380, height=500)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR, font=("arial", 10, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some question text", fill=THEME_COLOR, font=("Arial", 14, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # self.question = "Question text"
        # self.label2 = Label(padx=20, pady=20, width=25, height=10, text=f"{self.question}", fg=THEME_COLOR, bg="white", font=("verdana", 14, "italic"))
        # self.label2.grid(row=1, column=0, columnspan=2)

        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")

        self.true_button = Button(command=self.button_true, highlightthickness=0, image=true_img)
        self.true_button.grid(row=2, column=0)

        self.reset_button = Button(command=self.button_false, highlightthickness=0, image=false_img)
        self.reset_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of quiz, no more questions.")
            self.true_button.config(state="disabled")
            self.reset_button.config(state="disabled")



