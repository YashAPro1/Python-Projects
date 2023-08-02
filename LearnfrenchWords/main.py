import math
import pandas
import random
from tkinter import *
import time

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# <-------------------------------------create random word------------------------------->
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient='records')
current_card = {}

def flipcard():
    canvas.itemconfig(ctitle,text='English')
    canvas.itemconfig(cword,text=current_card['English'])
    canvas.itemconfig(myimage,image=backcard)
def create_word():
    global current_card,fliptime
    window.after_cancel(fliptime)
    canvas.itemconfig(myimage, image=frontcard)
    current_card = random.choice(to_learn)
    french_words = current_card['French']
    canvas.itemconfig(ctitle,text='French')
    canvas.itemconfig(cword,text=french_words)
    fliptime = window.after(3000, func=flipcard)

window = Tk()
window.title("FlashCard")
window.config(padx=20,pady=20)

fliptime = window.after(3000, func=flipcard)

canvas = Canvas(height=600,width=900,highlightthickness=0)
frontcard = PhotoImage(file="images/card_front.png",width=800,height=526)
backcard = PhotoImage(file="images/card_back.png",width=800,height=526)
myimage = canvas.create_image(450,300,image=frontcard)
ctitle =canvas.create_text(450,150,text="French",fill="RED",font=(FONT_NAME,30,"bold"))
cword =canvas.create_text(450,263,text="00:00",fill="PINK",font=(FONT_NAME,30,"bold"))

canvas.grid(row=1,column=1,columnspan=2)

rightpic = PhotoImage(file="images/right.png")
rightbutton = Button(image=rightpic,highlightthickness=0,command=create_word)

wrongpic =PhotoImage(file="images/wrong.png")
wrongbutton = Button(image=wrongpic)

rightbutton.grid(row=2,column=2,padx=10,pady=10)
wrongbutton.grid(row=2,column=1,padx=10,pady=10)

create_word()

window.mainloop()

