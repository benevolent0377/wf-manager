from tkinter import *

def foods():
    if x.get()==0:
        print("Pizza")
    elif x.get()==1:
        print("Hamburger")
    elif x.get()==2:
        print("Hotdog")


window = Tk()

food = ['pizza', 'hamburger', 'hotdog']
x = IntVar()

for i in range(len(food)):
    radiobutton = Radiobutton(window, text=food[i], variable=x, value=i, indicatoron=0, command=foods)
    radiobutton.pack(anchor="w")




window.mainloop()
