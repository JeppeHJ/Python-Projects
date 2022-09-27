BACKGROUND_COLOR = "#B1DDC6"
import pandas
from tkinter import *
import random
import csv
import os.path

word_data = pandas.read_csv("data/french_words.csv")

word_dict = {row.French:row.English for (index, row) in word_data.iterrows()}
new_dict = {}

def generate_word():
     global current_word
     new_word = random.choice(list(word_dict.keys()))
     current_word = new_word
     canvas.itemconfig(word, text=new_word)

def flip_card_english():
     canvas.itemconfig(title, text="English", fill="white")
     canvas.itemconfig(canvas_image, image=card_back)
     canvas.itemconfig(word, text=word_dict[current_word], fill="white")

def flip_card_french():
     global timer
     global current_word
     global new_dict
     window.after_cancel(timer)
     if os.path.exists("words_to_learn.csv"):
          dict_data = pandas.read_csv("words_to_learn.csv")
          new_dict = {row:row for (index, row) in dict_data.iterrows()}
          new_word = random.choice(list(new_dict.keys()))
          new_dict.pop(current_word)
          current_word = new_word
          new_page = pandas.DataFrame.from_dict(new_dict, orient="index")
          new_page.to_csv("words_to_learn.csv", index=True)
          canvas.itemconfig(title, text="French", fill="black")
          canvas.itemconfig(canvas_image, image=card_front)
          canvas.itemconfig(word, text=new_word, fill="black")
     else:
          new_word = random.choice(list(word_dict.keys()))
          new_dict = word_dict.copy()
          new_dict.pop(current_word)
          current_word = new_word
          new_page = pandas.DataFrame.from_dict(new_dict, orient="index")
          new_page.to_csv("words_to_learn.csv", index=True)
          canvas.itemconfig(title, text="French", fill="black")
          canvas.itemconfig(canvas_image, image=card_front)
          canvas.itemconfig(word, text=new_word, fill="black")
     timer = window.after(3000, flip_card_english)

window = Tk()
window.title("Jeppes Flash Card Game")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, flip_card_english)
print(timer)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas = Canvas(bg=BACKGROUND_COLOR, width=800, height=528, highlightthickness=0)
canvas_image = canvas.create_image(400, 260, image=card_front)
word = canvas.create_text(400, 263, text="French", font=("Arial", 60, "italic"))
title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
canvas.grid(column=0, row=0, columnspan=2)




#Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=flip_card_french)
wrong_button.grid(column=0, row=1)
correct_image = PhotoImage(file="images/right.png")
right_button = Button(image=correct_image, highlightthickness=0, command=flip_card_french)
right_button.grid(column=1, row=1)



generate_word()




window.mainloop()
