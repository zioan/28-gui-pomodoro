from tkinter import *
import math
from tkinter import font


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    global reps
    reps = 0

    work_min.config(state="normal")
    short_pause.config(state="normal")
    long_pause.config(state="normal")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    work_min.config(state="disabled")
    short_pause.config(state="disabled")
    long_pause.config(state="disabled")
    pop_up()

    global reps
    reps += 1
    work_sec = int(work_min.get()) * 60
    short_break_sec = int(short_pause.get()) * 60
    long_break_sec = int(long_pause.get()) * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
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
        check = "✔"
        total_check = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            total_check += check
        checkmark.config(text=total_check)


def pop_up():
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)  # bg is background


work_min_label = Label(text="Working minutes", bg=YELLOW)
work_min_label.grid(column=0, row=1)

work_min = Entry(width=6)
work_min.insert(0, 25)
work_min.grid(column=0, row=2)


short_pause_label = Label(text="Short pause", bg=YELLOW)
short_pause_label.grid(column=0, row=3)

short_pause = Entry(width=6)
short_pause.insert(0, 5)
short_pause.grid(column=0, row=4)


long_pause_label = Label(text="Long pause", bg=YELLOW)
long_pause_label.grid(column=0, row=5)

long_pause = Entry(width=6)
long_pause.insert(0, 20)
long_pause.grid(column=0, row=6)


start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=7)


reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=0, row=8)


title_label = Label(text="Timer", font=(FONT_NAME, 45, "bold"),
                    fg=GREEN, bg=YELLOW)  # fg is text color (foreground)
title_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW,
                highlightthickness=0)  # highlightthickness is border
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1, rowspan=8)


checkmark = Label(width=20, height=1, fg=GREEN, bg=YELLOW,
                  font=(FONT_NAME, 16, "normal"))
checkmark.grid(column=1, row=9)


window.mainloop()
