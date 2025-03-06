# basic tkinter gui
#

from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("Basic Tkinter Window") 

icon = PhotoImage(file="icon.png")
window.iconphoto(True, icon)

window.config(background="#222222")

window.mainloop()
