from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
SCORE = 0

# GET DATA
language_data = pandas.read_csv('hindi_converted.csv')
questions = language_data['hindi'].to_list()
answers = language_data['english'].to_list()

current_pos = 0


# FLASH CARD GENERATOR
def new_card():
    global current_pos
    current_pos = random.randint(0, len(questions))
    flash_card.itemconfig(language_text, text='Hindi')
    flash_card.itemconfig(word_text, text=questions[current_pos])
    flash_card.update()
    for i in range(30, -1, -1):
        flash_card.itemconfig(time_left_text, text=str(i))
        flash_card.update()
        window.after(1000)
    give_meaning()


def give_meaning():
    flash_card.itemconfig(language_text, text='English')
    flash_card.itemconfig(word_text, text=answers[current_pos])
    flash_card.update()
    for i in range(10, -1, -1):
        flash_card.itemconfig(time_left_text, text=str(i))
        flash_card.update()
        window.after(1000)


def correct_answer():
    global SCORE
    SCORE += 1
    flash_card.itemconfig(score_text, text=str(SCORE))
    give_meaning()
    new_card()


def wrong_answer():
    give_meaning()
    new_card()


# UI Setup

# Window
window = Tk()
window.title('Learn Hindi')
window.config(padx=100, pady=100, bg=BACKGROUND_COLOR)

# Images
correct_image = PhotoImage(file='images/tick_small.png')
incorrect_image = PhotoImage(file='images/cross_small.png')

# Window elements
flash_card = Canvas(width=800, height=500, bg='white', cursor='dot')
flash_card.grid(row=0, column=0, columnspan=2)
correct_btn = Button(image=correct_image, width=50, height=50, highlightthickness=0,
                     command=correct_answer)
correct_btn.grid(row=1, column=0)
incorrect_btn = Button(image=incorrect_image, width=50, height=50, highlightthickness=0, command=wrong_answer)
incorrect_btn.grid(row=1, column=1)

# Flash card content
language_text = flash_card.create_text(400, 150, fill="darkblue", font="Arial 20 bold",
                                       text="Language")
word_text = flash_card.create_text(400, 250, fill="darkblue", font="Arial 35 bold",
                                   text="Word")
score_text = flash_card.create_text(400, 50, fill="darkblue", font="Arial 10 bold",
                                    text="Score")
time_left_text = flash_card.create_text(400, 100, fill="darkblue", font="Arial 10 bold",
                                        text="Time Left")

new_card()
