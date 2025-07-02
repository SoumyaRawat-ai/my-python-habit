from tkinter import *

from kwarg import calculate
def calculates():
    ans = float(entry.get()) * 1.60934
    Answer['text'] = int(ans)

window = Tk()
window.minsize(width=300, height=100)
window.title("Mile to Km Converter")

window.config(padx=20, pady=20)

entry = Entry(width=10)
entry.insert(END, "0")
entry.grid(row=0, column=1)


equal_to = Label()
equal_to.config(text= "is equal to")
equal_to.grid(row=1, column=0)
equal_to.config(padx= 10, pady= 1-0)

Mile = Label()
Mile.config(text="Miles")
Mile.grid(row=0,column=2)

Answer = Label()
Answer.config(text="0")
Answer.grid(row=1, column=1)

km = Label()
km.config(text= 'Km')
km.grid(row=1, column=2)

Calculate = Button()
Calculate.config(text="Calculate", command= calculates)
Calculate.grid(row=2, column=1)

window.mainloop()