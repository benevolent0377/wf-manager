from tkinter import *

def display():
    if(x.get()==1):
        print("I like Python")
    elif(x.get()==0):
        print("I don't like Python")
    if(y.get()==1):
        print("I like Java.")
    elif(y.get()==0):
        print("I don't like Java...")

window = Tk()

x = IntVar()
y = IntVar()

checkbox = Checkbutton(window, text="Python", variable=x, onvalue=1, offvalue=0, command=display)
checkbox2 = Checkbutton(window, text='Java', variable=y, onvalue=1, offvalue=0, command=display)
checkbox.pack(side='left')
checkbox2.pack(side='left')
checkbox.config(anchor='w') # anchor the check box to the left of the window
checkbox2.config(anchor='w')

window.mainloop()
