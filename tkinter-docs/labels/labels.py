from tkinter import *

window = Tk()

photo = PhotoImage(file="photo.png")

label = Label(window, text="This is a label!", font=("Arial",40 , "bold"), fg="#00FF00", bg="#111111", relief=RAISED, bd=10, padx=20, pady=20, image=photo, compound=BOTTOM)
label.pack()
#label.place(x, y)
#label.grid(column, row)

window.mainloop()
