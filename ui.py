from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.label = Label(text="Score : 0", fg="white", bg=THEME_COLOR)
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(background="white", height=250, width=300)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.text = self.canvas.create_text(150, 125, text="question",
                                            fill=THEME_COLOR, font=("Arial", 20, "italic"),
                                            width=280)

        true_image = PhotoImage(file="true.png")
        self.button1 = Button(image=true_image, command=self.true_press)
        self.button1.grid(row=2, column=0)
        false_image = PhotoImage(file="false.png")
        self.button2 = Button(image=false_image, command=self.false_press)
        self.button2.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the quiz")
            self.button1.config(state="disabled")
            self.button2.config(state="disabled")

    def true_press(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_press(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, func=self.get_next_question)
