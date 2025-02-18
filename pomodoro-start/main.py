import math
import tkinter
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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="Timer")
    chck_label.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_mech():
    global reps
    work_sec = WORK_MIN*10
    short_breck_sec = SHORT_BREAK_MIN*10
    long_break_sec = LONG_BREAK_MIN*60
    if reps%2==0:
        my_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps%7==0:
        my_label.config(text="Break", fg=PINK)
        count_down(long_break_sec)
    else:
        my_label.config(text="Break", fg=RED)
        count_down(short_breck_sec)
    reps+=1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec <=9:
        count_sec = f"0{count_sec}"
    if count_min <=9:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        timer_mech()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✓"
        chck_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomao_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image= tomao_img)
timer_text = canvas.create_text(100,130,text="00:00", fill= "White", font=(FONT_NAME, 35,"bold"))
canvas.grid(column = 2, row= 2)

#label
my_label = tkinter.Label(text="Timer",bg=YELLOW, fg= GREEN, font=("Arial", 28, "bold"))
my_label.grid(column= 2, row= 1)

chck_label = tkinter.Label(bg=YELLOW, fg= GREEN, font=("Arial", 14, "bold"))
chck_label.grid(column= 2, row= 4)

#Button
start_button = tkinter.Button(text="Start", font=("Arial", 12), highlightthickness=0, command=timer_mech)
start_button.grid(column= 1, row= 3)

reset_button =tkinter.Button(text="Reset", font=("Arial", 12), highlightthickness=0, command=reset)
reset_button.grid(column= 3, row= 3)


window.mainloop()