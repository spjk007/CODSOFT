from tkinter import *
problem=""
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

if __name__=="__main__":
    cal=Tk()
    cal.title("4way Calculator")
    cal.config(bg="lightgray")
    noenter=StringVar()
    evaluatingcell=Entry(cal,textvariable=noenter,width=40,borderwidth=5)
    evaluatingcell.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
    NO_1=Button(cal,text="1",padx=25,pady=10,command=lambda:clicknumbers(1),activebackground="red",activeforeground="yellow",bg="lightgray",fg="navy",borderwidth=3)
    NO_2=Button(cal,text="2",padx=25,pady=10,command=lambda:clicknumbers(2),activebackground="red",activeforeground="yellow",bg="lightgray",fg="navy",borderwidth=3)
    NO_3=Button(cal,text="3",padx=25,pady=10,command=lambda:clicknumbers(3),activebackground="red",activeforeground="yellow",bg="lightgray",fg="navy",borderwidth=3)
    NO_4=Button(cal,text="4",padx=25,pady=10,command=lambda:clicknumbers(4),activebackground="red",activeforeground="yellow",bg="lightgray",fg="navy",borderwidth=3)
    NO_5=Button(cal,text="5",padx=25,pady=10,command=lambda:clicknumbers(5),activebackground="red",activeforeground="yellow",bg="lightgray",fg="navy",borderwidth=3)
    NO_6=Button(cal,text="6",padx=25,pady=10,command=lambda:clicknumbers(6),activebackground="red",activeforeground="yellow",bg="lightgray",fg="navy",borderwidth=3)
    NO_7=Button(cal,text="7",padx=25,pady=10,command=lambda:clicknumbers(7),activebackground="red",activeforeground="yellow",bg="lightgray",fg="navy",borderwidth=3)
    NO_8=Button(cal,text="8",padx=25,pady=10,command=lambda:clicknumbers(8),activebackground="red",activeforeground="yellow",bg="lightgray",fg="navy",borderwidth=3)
    NO_9=Button(cal,text="9",padx=25,pady=10,command=lambda:clicknumbers(9),activebackground="red",activeforeground="yellow",bg="lightgray",fg="navy",borderwidth=3)
    NO_0=Button(cal,text="0",padx=25,pady=10,command=lambda:clicknumbers(0),activebackground="red",activeforeground="yellow",bg="lightgray",fg="navy",borderwidth=3)
    addbutton=Button(cal,text="+",padx=21,pady=10,command=lambda:clicknumbers("+"),activebackground="red",activeforeground="yellow",bg="lightgray",fg="navy",borderwidth=3)
    subbutton=Button(cal,text="-",padx=22,pady=10,command=lambda:clicknumbers("-"),activebackground="red",activeforeground="yellow",bg="lightgray",fg="navy",borderwidth=3)
    mulbutton=Button(cal,text="x",padx=22,pady=10,command=lambda:clicknumbers("*"),activebackground="red",activeforeground="yellow",bg="lightgray",fg="navy",borderwidth=3)
    divbutton=Button(cal,text="/",padx=22,pady=10,command=lambda:clicknumbers("/"),activebackground="red",activeforeground="yellow",bg="lightgray",fg="navy",borderwidth=3)
    equalbutton=Button(cal,text="clr",padx=24,pady=10,command=clickclear,activebackground="red",activeforeground="yellow",bg="lightblue",fg="navy",borderwidth=3)
    clearbutton=Button(cal,text="=",padx=22,pady=10,command=clickequal,activebackground="red",activeforeground="yellow",bg="lightgray",fg="navy",borderwidth=3)
    NO_1.grid(row=1,column=0)
    NO_2.grid(row=1,column=1)
    NO_3.grid(row=1,column=2)
    NO_4.grid(row=2,column=0)
    NO_5.grid(row=2,column=1)
    NO_6.grid(row=2,column=2)
    NO_7.grid(row=3,column=0)
    NO_8.grid(row=3,column=1)
    NO_9.grid(row=3,column=2)
    NO_0.grid(row=4,column=0)
    addbutton.grid(row=1,column=3)
    subbutton.grid(row=2,column=3)
    mulbutton.grid(row=3,column=3)
    divbutton.grid(row=4,column=3)
    equalbutton.grid(row=4,column=1)
    clearbutton.grid(row=4,column=2)
    cal.resizable(False,False)
    
    cal.mainloop()
    
    
