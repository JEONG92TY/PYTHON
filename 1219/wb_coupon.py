import random
from tkinter import *

def on_click():
    name_list = ["1", "2", "3", "4", "5"]

    #name = random.sample(name_list, 2)
    name = name_list[0:3]
    text.delete("1.0", END)
    text.insert(END, name)

window = Tk()
window.title("Coupon")
window.geometry("640x480")

#label_img = Label(window)
#img = PhotoImage(file="./1218/test.png")
#label_img.config(image=img)
#label_img.pack()

Button(window, text="추첨", command=on_click).pack()

text = Text(window, width=40 , height=5 , bg="green")
text.pack()

window.mainloop()