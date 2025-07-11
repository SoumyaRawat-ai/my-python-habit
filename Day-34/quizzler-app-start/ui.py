from tkinter import *
from quiz_brain import QuizBrain
from tkinter import PhotoImage
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = Label(text=f'score: 0', background=THEME_COLOR, fg='white', font= 'Arial 14')
        self.score.grid(row=0, column=1, pady=20, padx=20)
        self.can = self.canvas = Canvas(self.window, width= 300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text=f'All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.',width=280,  font='Arial 16 italic')
        self.canvas.grid(row=1,column=0, columnspan=2,pady= 30, padx= 20 )
        false_img = PhotoImage(file=r'../quizzler-app-start/images/false.png')
        self.false = Button(image= false_img, command=self.false_pressed)
        self.false.grid(row=2,column=0, pady=20)
        true_img = PhotoImage(file=r'../quizzler-app-start/images/true.png')
        self.true = Button(image=true_img, command=self.true_pressed)
        self.true.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background='white')
        if self.quiz_brain.still_has_questions():
            self.score.config(text=f"Score: {self.quiz_brain.score}")
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end of the quiz.')
            self.true.config(state='disable')
            self.false.config(state='disable')
    def true_pressed(self):
        is_right = self.quiz_brain.check_answer("True")
        self.give_feedback(is_right)
    def false_pressed(self):
        is_right = self.quiz_brain.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background='green')
            self.window.after(1000, self.get_next_question)


        else:
            self.canvas.config(background='red')
        self.window.after(1000, self.get_next_question)


    def set_canvas_w(self):
        self.canvas.config(background='white')