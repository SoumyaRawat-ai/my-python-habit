import tkinter

def button_clicked():
    my_label['text'] = input.get()

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width = 500, height= 300)
window.config(padx=100, pady=100)

#Label
my_label = tkinter.Label(text= "I am a Label", font= ("Arial", 24))
my_label["text"] = "New text"
my_label.config(text= "helo label")
# my_label.pack()
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

button = tkinter.Button(text="Click me", command=button_clicked)
# button.place(x=100,y=200)
button.grid(column=1, row=1)


button2 = tkinter.Button(text="click me too")
button2.grid(column=2, row=0)

#Enter
input = tkinter.Entry()
# input.pack()
input.grid(column=3,row=3)




window.mainloop()