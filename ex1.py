from tkinter import *

problem = ""

def clicknumbers(no):
    global problem
    problem = problem + str(no)
    noenter.set(problem)

def clickequal():
    try:
        global problem
        solve = str(eval(problem))
        noenter.set(solve)
        problem = ""
    except:
        noenter.set("Error")
        problem = ""

def clickclear():
    global problem 
    problem = "" 
    noenter.set("") 

if __name__ == "__main__":
    cal = Tk()
    cal.title("Calculator")

    noenter = StringVar()
    noenter.set("")

    entry = Entry(cal, textvariable=noenter, font=('arial', 20, 'bold'), bd=15, insertwidth=4, width=14, justify='right')
    entry.grid(row=0, column=0, columnspan=4)

    numbers = [
        '7', '8', '9',
        '4', '5', '6',
        '1', '2', '3',
        '0'
    ]

    row_val = 1
    col_val = 0
    for number in numbers:
        Button(cal, text=number, padx=20, pady=20, font=('arial', 20, 'bold'), bd=8, command=lambda num=number: clicknumbers(num)).grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 2:
            col_val = 0
            row_val += 1

    Button(cal, text='C', padx=20, pady=20, font=('arial', 20, 'bold'), bd=8, command=clickclear).grid(row=4, column=0)
    Button(cal, text='=', padx=20, pady=20, font=('arial', 20, 'bold'), bd=8, command=clickequal).grid(row=4, column=1, columnspan=2)

    operators = ['+', '-', '*', '/']
    row_val = 1
    col_val = 3
    for operator in operators:
        Button(cal, text=operator, padx=20, pady=20, font=('arial', 20, 'bold'), bd=8, command=lambda op=operator: clicknumbers(op)).grid(row=row_val, column=col_val)
        row_val += 1

    cal.mainloop()
