import random
from tkinter import *
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    data = pd.read_csv("data/words_to_learn.csv",encoding="UTF-8")
except FileNotFoundError:
    original_data = pd.read_csv("data/hindi_words.csv",encoding="UTF-8")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_cards():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    current_card["Hindi"]
    canvas.itemconfig(card_title, text = "Hindi", fill="black")
    canvas.itemconfig(card_word, text = current_card["Hindi"], fill="black")
    canvas.itemconfig(card_background, image = card_front_img)
    flip_timer = window.after(3000, func = flip_card)


def flip_card():
    canvas.itemconfig(card_title, text = "English", fill="white")
    canvas.itemconfig(card_word, text = current_card["English"], fill="white")
    canvas.itemconfig(card_background, image = card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", encoding="UTF-8", index=False)
    next_cards()
    


window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=30, pady=30)

flip_timer = window.after(3000, func = flip_card)



canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")


card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text = "", font = ("Areil",40,"italic"))
card_word = canvas.create_text(400, 263, text = "", font = ("Areil",60,"bold"))


canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0, columnspan = 2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_cards)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)


next_cards()

window.mainloop()
