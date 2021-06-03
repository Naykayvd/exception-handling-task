import tkinter as tk
from tkinter import *
from tkinter import messagebox

window = tk.Tk()
window.geometry("300x300")
window.title("exception handling")

def check():
    if int(amount_entry.get()) >= 3000:
        raise messagebox.showinfo("status feedback","Congratulations. You qualify to go to Malaysia.")
    else:
        raise messagebox.showinfo("Status feedback","Please deposit more funds for this excursion.")

amount_label = Label(window, text='please enter your amount')
amount_label.place(x=70, y=60)
amount_entry = Entry(window)
amount_entry.place(x=75,y=90)
amount_button = Button(window, text='check qualification', command=check)
amount_button.place(x=84, y= 150)
window.mainloop()