import tkinter as tk
from tkinter import *
from tkinter import messagebox

window = tk.Tk()
window.geometry("400x400")
window.title("Authentification")

user_pass = {'Nahum': 'nahum2021', 'Devin': 'devin2021', 'Shuaib': 'shuaib2021', 'Jason': 'jason2021'}


def enter():
    user_name = username_entry.get()
    pass_word = password_entry.get()

    if user_name in user_pass and user_pass[user_name] == pass_word:
        messagebox.showinfo("good", "Password is correct")
        window.destroy()
        import task2
    else:
        messagebox.showerror("wrong login details", "incorrect username and/or password")


login_details = Label(window, text="please enter your login details")
login_details.place(x=100, y=10)
username_label = Label(window, text="username")
username_label.place(x=70, y=80)
username_entry = Entry(window)
username_entry.place(x=140, y=80)
password_label = Label(window, text="password")
password_label.place(x=70, y=120)
password_entry = Entry(window)
password_entry.place(x=140, y=120)
login_button = Button(window, text="login", command=enter)
login_button.place(x=180, y=200)

window.mainloop()
