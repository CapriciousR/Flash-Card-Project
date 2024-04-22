from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# Generate new words
try:
    data = pandas.read_csv("data/words_to_learn.csv") 
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    data.to_csv("data/words_to_learn.csv")
finally:    
    word_dict = data.to_dict(orient="records")
    current_word = {}

def generateWord():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = choice(word_dict)
    canvas.itemconfig(canvas_img, image = card_front_img)
    canvas.itemconfig(title_text, text = "French")
    canvas.itemconfig(word_text, text = current_word["French"])
    flip_timer = window.after(3000, func=flipCard)

# Flip Card 
   
def flipCard():
    global current_word
    canvas.itemconfig(canvas_img, image = card_back_img)
    canvas.itemconfig(title_text, text = "English")
    canvas.itemconfig(word_text, text = current_word["English"])
    
# Right button

def right_clicked():
    global current_word
    word_dict.remove(current_word)
    temp = pandas.DataFrame(word_dict)
    temp.to_csv("data/words_to_learn.csv", index=False)
    generateWord()
        
               
# UI Setup

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flipCard)

canvas = Canvas(height=526, width=800)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

canvas_img = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400,150,text="Title", font=("Ariel",40,"italic"))
word_text = canvas.create_text(400,263,text="Word", font=("Ariel", 60, "bold"))

canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image = right_image, highlightthickness=0, command=right_clicked)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image = wrong_image, highlightthickness=0, command=generateWord)
wrong_button.grid(row=1, column=0)

generateWord()

window.mainloop()