from tkinter import *

def submit():

    food = []

    for i in listbox.curselection():
        food.insert(i, listbox.get(i))

    print("You have ordered ")

    for i in food:
        print(i, end=", ")

    print(".")

def add():
    listbox.insert(listbox.size(), entry.get())
    listbox.config(height=listbox.size())

def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)

    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window, bg="#ffffff", font=("Contstantia", 35), width=12, selectmode=MULTIPLE)
listbox.pack()


listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")


entry = Entry(window)
entry.pack()
add = Button(window, text="Add", command=add)
add.pack()
submit = Button(window, text="submit", command=submit)
submit.pack()
delete = Button(window, text="Delete", command=delete)
delete.pack()


listbox.config(height=listbox.size())

window.mainloop()
