from tkinter import *
import datetime

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None

# ----------------------------- GLOBAL VARIABLES -------------------------- #
rep_number = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global rep_number
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=datetime.timedelta(seconds=0))
    rep_number = 0
    title_label.config(text='Timer')
    check_label.config(text='')
    canvas.itemconfig(timer_text, text=datetime.timedelta(seconds=0))


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global rep_number
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    rep_number += 1
    if not rep_number % 2 == 0 and rep_number < 8:
        # Time to work
        count_down(work_time)
        title_label.config(text='Work')
    elif rep_number % 2 == 0 and rep_number < 8:
        # Short break time
        # Since work was done, add another check mark
        check_label.config(text=check_label.cget('text') + '✔')
        count_down(short_break)
        title_label.config(text='Short Break')
    elif rep_number == 8:
        rep_number = 0
        check_label.config(text='')
        # Long break time
        count_down(long_break)
        title_label.config(text='Long Break')


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    canvas.itemconfig(timer_text, text=datetime.timedelta(seconds=count))
    if count > 0:
        global timer
        timer = window.after(10, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# Setting up the window
window = Tk()
window.title('Pomodoro App')
window.config(padx=50, pady=50, bg=YELLOW)

# Canvas widget for placing an image and layer text on top of it
canvas = Canvas(width=200, height=250, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(100, 125, image=image)
timer_text = canvas.create_text(100, 140, text=datetime.timedelta(seconds=0), font=(FONT_NAME, 25, 'bold'))
canvas.grid(row=1, column=1)

# Buttons
reset_btn = Button(text='Reset', font=(FONT_NAME, 10, 'bold'), command=reset)
reset_btn.grid(row=2, column=2)
start_btn = Button(text='Start', font=(FONT_NAME, 10, 'bold'), command=start_timer)
start_btn.grid(row=2, column=0)

# Labels
title_label = Label(text='Timer', font=(FONT_NAME, 20, 'bold'), fg=RED, bg=YELLOW)
title_label.grid(row=0, column=1)
check_label = Label(text='', font=(FONT_NAME, 25, 'bold'), fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

window.mainloop()
