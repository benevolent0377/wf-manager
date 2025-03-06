from tkinter import *

count = 0
def click():
    global count
    count += 1
    Label.config(text=count)

window = Tk()

button = Button(window, text="Click Me")
button.config(command=click)#preform the call back of the function click
button.config(font=("Consolas", 50), bg="#ff6200")
button.config(activebackground="red")
picture = PhotoImage(file="photo.png")
button.config(image=picture, compound=BOTTOM)
Label = Label(window, text=count)
Label.config(font=('Consolas', 50))
Label.pack()
button.pack()


window.mainloop()
