from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_text_label.config(text="Timer")
    check_mark_label.config(text="")
    global reps
    reps = 0
    start_btn.config(state=ACTIVE)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    start_btn.config(state=DISABLED)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    active_sec = work_sec

    if reps % 8 == 0:
        title_text_label.config(text="Long Break", fg=RED)
        active_sec = long_break_sec
    elif reps % 2 == 0:
        title_text_label.config(text="Short Break", fg=PINK)
        active_sec = short_break_sec
    else:
        title_text_label.config(text="Work Time", fg=GREEN)
        active_sec = work_sec

    countdown(active_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += CHECK_MARK
        check_mark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PomPom Power")
window.config(padx=100, pady=50, bg=YELLOW)

title_text_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
title_text_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

start_btn = Button(text="Start", font=("Verdana", 10, "bold"), bg="white", command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", font=("Verdana", 10, "bold"), bg="white", command=reset_timer)
reset_btn.grid(row=2, column=2)

check_mark_label = Label(fg=GREEN, font=("bold"))
check_mark_label.grid(row=3, column=1)

window.mainloop()
