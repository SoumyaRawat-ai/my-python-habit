import random
from tkinter import *
from tkinter import PhotoImage
import pandas as pd
import time

from pandas.core.interchange.dataframe_protocol import DataFrame

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pd.read_csv(r'data/word_to_learn.csv')
except FileNotFoundError :
    data = pd.read_csv(r'../flash-card-project-start/data/french_words.csv')
except pd.errors.EmptyDataError:
    data = pd.read_csv(r'../flash-card-project-start/data/french_words.csv')
to_learn = data.to_dict('records')
# word = random.choice(to_learn)
word ={}
def right():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(to_learn)
    front_img.itemconfig(fi, image=fr_image)
    front_img.itemconfig(te1,text= 'French', fill= 'black')
    front_img.itemconfig(te,text=word['French'], fill='black')
    flip_timer =  window.after(3000, func=change)


def change():
    front_img.itemconfig(fi, image= bk_img)
    front_img.itemconfig(te1, text='English', fill= 'white')
    front_img.itemconfig(te, text=word['English'], fill = 'white')


def is_known():
    to_learn.remove(word)
    DataFrame = pd.DataFrame(to_learn)
    DataFrame.to_csv('data/word_to_learn.csv', index = False)
    right()
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50,pady=50)

flip_timer = window.after(3000, func=change)


bk_img = PhotoImage(file=r'images\card_back.png')
fr_image = PhotoImage(file=r'images\card_front.png')
front_img = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
fi = front_img.create_image(400, 263,image= fr_image)
te1 =front_img.create_text(400, 150, text='', font=("Ariel", 40, "italic"))
te = front_img.create_text(400, 263, text='', font=("Ariel", 60, "bold"))
front_img.grid(row=0, column=0, columnspan=2)



x_btn = PhotoImage(file=r'D:\PycharmProjects\Day-31\flash-card-project-start\images\wrong.png')
x = Button(image=x_btn, bg=BACKGROUND_COLOR, command=right)
x.grid(row=1, column=0)

y_btn = PhotoImage(file=r'D:\PycharmProjects\Day-31\flash-card-project-start\images\right.png')
y = Button(image=y_btn, bg=BACKGROUND_COLOR, command=is_known)
y.grid(row=1, column=1)

right()

window.mainloop()
