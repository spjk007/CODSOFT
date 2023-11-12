from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from tkinter import filedialog
import pickle

def deleteitem():
    listofitems.delete(ANCHOR)

def additem():
    item = enteritem.get().strip()  
    if item:
        # Get the current number of items in the list
        item_number = listofitems.size() + 1
        # Add the item with the item number
        listofitems.insert(END, f"{item_number}. {item}")
        enteritem.delete(0, END)
    else:
        messagebox.showwarning("Empty Entry", "Please enter an item.")

def crossitem():
    listofitems.itemconfig(listofitems.curselection(), fg="#dedede")
    listofitems.selection_clear(0, END)

def uncrossitem():
    listofitems.itemconfig(listofitems.curselection(), fg="#464646")
    listofitems.selection_clear(0, END)

def deletecrossitem():
    itemcount = 0
    while itemcount < listofitems.size():
        if listofitems.itemcget(itemcount, "fg") == "#dedede":
            listofitems.delete(listofitems.index(itemcount))
        else:
            itemcount += 1

def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir="C:/Users/hp/Datafilestdl",
        title="Save file",
        filetypes=(("TDL Files", ".tdl"), ("All Files", "*.*"))
    )
    if file_name:
        if not file_name.endswith(".tdl"):
            file_name = f'{file_name}.tdl'
        itemcount = 0
        while itemcount < listofitems.size():
            if listofitems.itemcget(itemcount, "fg") == "#dedede":
                listofitems.delete(listofitems.index(itemcount))
            else:
                itemcount += 1
        stuff = [listofitems.get(i) for i in range(listofitems.size())]
        output_file = open(file_name, 'wb')
        pickle.dump(stuff, output_file)
        output_file.close()

def open_list():
    file_name = filedialog.askopenfilename(
        initialdir="C:/Users/hp/Datafilestdl",
        title="Open file",
        filetypes=(("TDL Files", ".tdl"), ("All Files", "*.*"))
    )
    if file_name:
        input_file = open(file_name, 'rb')
        stuff = pickle.load(input_file)
        input_file.close()
        listofitems.delete(0, END)
        for i, item in enumerate(stuff, start=1):
            listofitems.insert(END, f"{i}. {item}")

def delete_list():
    listofitems.delete(0, END)

if __name__ == "__main__":
    tdl = Tk()
    tdl.title("Simply To-Do-List")
    my_font = Font(family="Times New Roman", size=25, weight="bold")
    tdl.geometry("450x400")
    my_frame = Frame(tdl)
    my_frame.pack(pady=10)
    listofitems = Listbox(my_frame, font=my_font, width=25, height=5, bg="SystemButtonFace", bd=0, fg="#464646",
                          highlightthickness=0, selectbackground="#a6a6a6", activestyle="none")
    listofitems.pack(side=LEFT, fill=BOTH)
    scroller = Scrollbar(my_frame)
    scroller.pack(side=RIGHT, fill=BOTH)
    listofitems.config(yscrollcommand=scroller.set)
    scroller.config(command=listofitems.yview)
    enteritem = Entry(tdl, font=("Helvitica", 24), width=24, borderwidth=5)
    enteritem.pack(pady=20)
    buttonframe = Frame(tdl)
    buttonframe.pack(pady=2)
    deletebutton = Button(buttonframe, text="Delete", command=deleteitem, font=("helvetica", 15), borderwidth=2,
                          bg="#66BEC5", fg="Black", activebackground="#BE66C5", activeforeground="#EC13C5")
    addbutton = Button(buttonframe, text="Add", command=additem, font=("helvetica", 15), width=8,borderwidth=2,
                       bg="#66BEC5", fg="Black", activebackground="#BE66C5", activeforeground="#EC13C5")
    crossbutton = Button(buttonframe, text="Cross Off", command=crossitem, font=("helvetica", 15), borderwidth=2,
                         bg="#66BEC5", fg="Black", activebackground="#BE66C5", activeforeground="#EC13C5")
    uncrossbutton = Button(buttonframe, text="Uncross", command=uncrossitem, font=("helvetica", 15), borderwidth=2,
                           bg="#66BEC5", fg="Black", activebackground="#BE66C5", activeforeground="#EC13C5")
    deletecrossbutton = Button(buttonframe, text="Delete All Crossed Off Items", command=deletecrossitem,
                               font=("helvetica", 15), borderwidth=2, bg="#66BEC5", fg="Black",
                               activebackground="#BE66C5", activeforeground="#EC13C5")
    deletebutton.grid(row=0, column=0, padx=10)
    addbutton.grid(row=0, column=1)
    crossbutton.grid(row=0, column=2, padx=10)
    uncrossbutton.grid(row=0, column=3)
    deletecrossbutton.grid(row=1, column=0, columnspan=4, pady=5)
    my_menu = Menu(tdl)
    tdl.config(menu=my_menu, )
    filemenu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Save List", command=save_list)
    filemenu.add_command(label="open list", command=open_list)
    filemenu.add_separator()
    filemenu.add_command(label="clear List", command=delete_list)
    tdl.resizable(False,False)
    tdl.mainloop()
