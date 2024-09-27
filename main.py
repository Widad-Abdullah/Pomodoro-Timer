from math import floor
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_count():
    window.after_cancel(timer)
    canvas.itemconfig(time, text=f"00:00")
    timer_label.config(text="Timer",fg=GREEN)
    check.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def handle_start():
    global reps
    reps += 1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps%8==0:
        count_down(long_break_sec)
        timer_label.config(text="Break",fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        timer_label.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    mins=floor(count/60)
    sec=count%60
    if sec < 10:
        sec=f"0{sec}"
    canvas.itemconfig(time,text=f"{mins}:{sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        handle_start()
        marks=""
        for _ in range(floor(reps/2)):
            marks+="✔"

        check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

timer_label=Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,35,'bold'))
timer_label.grid(column=1,row=0)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=img)
time=canvas.create_text(100,130,text="00:00", fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column=1,row=1)

start_button=Button(text="Start",command=handle_start)
start_button.grid(column=0,row=2)

check=Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME,15,'bold'))
check.grid(column=1,row=3)

reset_button=Button(text="Reset",command=reset_count)
reset_button.grid(column=2,row=2)

window.mainloop()