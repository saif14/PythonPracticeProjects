from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
TRUE = "#B6E388"
FALSE = "#F96666"
FINISHED = "#FBF2CF"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.score.grid(row=0, column=1, sticky="e")

        self.canvas = Canvas(bg="white", width=300, height=250, )
        self.question_text = self.canvas.create_text(150, 125, text="Some Question", fill=THEME_COLOR,
                                                     font=("Aria", 20, "italic"),
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_btn = Button(image=true_img, highlightthickness=0, borderwidth=0, bg=THEME_COLOR,
                               command=self.true_btn_click)
        self.true_btn.grid(row=2, column=0)
        self.false_btn = Button(image=false_img, highlightthickness=0, borderwidth=0, bg=THEME_COLOR,
                                command=self.false_btn_click)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def btn_handle(self, ans):
        res = self.quiz.check_answer(ans)
        if res:
            self.canvas.config(bg=TRUE)
        else:
            self.canvas.config(bg=FALSE)

        self.score.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_question)

    def true_btn_click(self):
        self.btn_handle("true")

    def false_btn_click(self):
        self.btn_handle("false")

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Quiz Finished \nTotal Score:{self.quiz.score}/10")
            self.canvas.config(bg=FINISHED)
            self.true_btn.config(state=DISABLED)
            self.false_btn.config(state=DISABLED)
