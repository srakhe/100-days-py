from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quizBrain = quiz

        self.window = Tk()
        self.window.title('Quizzy Game')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125,
                                                     text='Question text', fill=THEME_COLOR,
                                                     width=280,
                                                     font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file='images/true.png')
        self.true_btn = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_btn.grid(row=2, column=0)

        false_image = PhotoImage(file='images/false.png')
        self.false_btn = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quizBrain.still_has_questions():
            q_text = self.quizBrain.next_question()
        else:
            q_text = 'The end!'
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')
        self.score_label.config(text=f'Score: {self.quizBrain.score}')
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        result = self.quizBrain.check_answer('True')
        self.verify_answer(result)

    def false_pressed(self):
        result = self.quizBrain.check_answer('False')
        self.verify_answer(result)

    def verify_answer(self, result):
        if result:
            self.canvas.config(bg='green')
            self.window.update()
            self.window.after(1000, self.canvas.config(bg='white'))
        else:
            self.canvas.config(bg='red')
            self.window.update()
            self.window.after(1000, self.canvas.config(bg='white'))
        self.canvas.config(bg='white')
        self.get_next_question()
