from tkinter import *
import math
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FFB4B4"
RED = "#E14434"
BLUE = "#5EABD6"
YEllOW = "#FEFBC7"
GREEN = "#9bdeac"

FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
t = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    window.after_cancel(t)
    timer["text"] = "Timer"
    canvas.itemconfig(timer_text, text=f"00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def strat_timer():
    global reps
    if reps == 0:
        reps += 1
        work_sec = WORK_MIN * 60
        short_break = SHORT_BREAK_MIN * 60
        long_break= LONG_BREAK_MIN * 60
        if reps%8 ==0:
            count_down(long_break)
            timer['fg'] = RED
            timer['text'] = "Long  Break"
        elif reps%2 ==0:
            count_down(short_break)
            timer['fg'] = PINK
            timer['text'] = "Short Break"
        else:
            timer['text'] = "Work Min"
            timer['fg'] = GREEN
            count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    c = 0
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_sec == 0:
        count_sec = "00"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global t
        t = window.after(1000, count_down, count - 1)
    else:
        strat_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔️"
        tick['text'] = marks
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YEllOW)
# window.maxsize(width=600, height= 400 )



canvas = Canvas(width=200, height=224, bg=YEllOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 129, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
# count_down(5)

timer = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=BLUE, bg=YEllOW)
timer.grid(column= 1, row=0)

start = Button(text="Start", highlightthickness=0, command=strat_timer)
start.grid(column=0, row=2)

reset = Button(text='Reset', highlightthickness=0, command=reset_time)
reset.grid(column=2, row=2)

tick = Label(bg=YEllOW, fg=BLUE, highlightthickness=0, font=(FONT_NAME, 12))
tick.config(pady=5, padx=5)
tick.grid(column=1, row=3)







window.mainloop()