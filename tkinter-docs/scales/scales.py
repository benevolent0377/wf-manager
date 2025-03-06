from tkinter import *

def submit():
    print("The temperature is " + str(scale.get()) + " degrees C.") 


window = Tk()

scale = Scale(window, from_=100, to_=0, length=600, font=("Arial", 20), tickinterval=10, troughcolor = "#69eaff", fg="#FF1c00", bg="#222222")
# you can also change the orientation, using orient=VERTICAL or HORIZONTAL
# showvalue hides the current value of the slider. set it to 0 if you dont want it to show

scale.set(45)
scale.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()
