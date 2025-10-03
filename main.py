import math
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
CHECKMARK = "✔"

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer
    if timer is not None:
        window.after_cancel(timer)  # Stop current timer

    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:  # Long break
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:  # Short break
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
    else:  # Work
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = CHECKMARK * (reps // 2)
        check_label.config(text=marks)
        window.bell()  # Play sound when timer ends (works in most OS)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", width=10, highlightthickness=0, command=start_timer, bg=GREEN, fg="white")
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", width=10, highlightthickness=0, command=reset_timer, bg=RED, fg="white")
reset_button.grid(row=2, column=2)

check_label = Label(font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
check_label.grid(row=3, column=1, pady=20)

window.mainloop()
