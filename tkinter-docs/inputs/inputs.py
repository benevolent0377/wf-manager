from tkinter import *

def submit():
    username = entry.get()
    print(username)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()
window.config(bg="#222222")

submit = Button(window, text="submit", command=submit)
backspace = Button(window, text='Backspace', command=backspace, padx=20, pady=20)
delete = Button(window, text="Delete", command=delete)

entry = Entry()
entry.config(font=("Arial", 50))
entry.config(bg="#222222")
entry.config(fg="green")

#entry.insert(0, "Inserted Text")
#entry.config(state=DISABLED)
#entry.config(show="*")

entry.config(width=50)
entry.pack()
submit.pack()
delete.pack(side= RIGHT)
backspace.pack(side= RIGHT)

window.mainloop()
