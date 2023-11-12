from tkinter import *
from tkinter.font import Font
import random
import pyperclip
from tkinter.ttk import *

def password():
    passwordentry.delete(0, END)
    length = variable1.get()
    easy = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    hard = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    pas = ""

    if variable.get() == 1:
        for i in range(0, length):
            pas = pas + random.choice(easy)
    elif variable.get() == 2:
        for i in range(0, length):
            pas = pas + random.choice(hard)
    elif variable.get() == 3:
        for i in range(0, length):
            pas = pas + chr(random.randint(33, 126))

    passwordentry.insert(0, pas)

def clipper():
    random_password = passwordentry.get()
    pyperclip.copy(random_password)

def generate():
    password()

if __name__ == "__main__":
    rpg = Tk()
    rpg.title("Password Generator")
    rpg.geometry("400x150")
    my_font = Font(family="Times New Roman", size=15, weight="bold")
    variable = IntVar()
    variable1 = IntVar()

    # Adding a style for Radiobutton and Button
    style = Style()
    style.configure("TRadiobutton", font=("serif", 12))
    style.configure("TButton", font=("serif", 12), background="#f1c3fd", activebackground="#ececb4")

    passwordframe = Frame(rpg)
    passwordframe.pack(padx=10, pady=10)

    passwordlabel = Label(passwordframe, text="PASSWORD:", font=my_font)
    passwordentry = Entry(passwordframe)
    lengthlabel = Label(passwordframe, text="LENGTH:", font=my_font)
    lengthentry = Combobox(passwordframe, textvariable=variable1)
    lengthentry['values'] = (6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, "Length")
    lengthentry.current(0)

    lowbutton = Radiobutton(passwordframe, text="EASY", variable=variable, value=1, style="TRadiobutton")
    mediumbutton = Radiobutton(passwordframe, text="HARD", variable=variable, value=2, style="TRadiobutton")
    strongbutton = Radiobutton(passwordframe, text="COMPLEX", variable=variable, value=3, style="TRadiobutton")
    generatebutton = Button(passwordframe, text="GENERATE", command=generate, style="TButton")
    clipbutton = Button(passwordframe, text="COPY TO CLIPBOARD", command=clipper, style="TButton")

    passwordlabel.grid(row=0, column=0)
    passwordentry.grid(row=0, column=1)
    lengthlabel.grid(row=1, column=0)
    lengthentry.grid(row=1, column=1)
    lowbutton.grid(row=2, column=0, sticky="EW")
    mediumbutton.grid(row=2, column=1, sticky="EW")
    strongbutton.grid(row=2, column=2, sticky="EW")
    generatebutton.grid(row=3, column=0)
    clipbutton.grid(row=3, column=1)
    rpg.resizable(False, False)
    rpg.mainloop()
