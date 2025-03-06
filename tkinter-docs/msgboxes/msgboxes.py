from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title="Notification", message="You have clicked the button.")
    #messagebox.showwarning(title="Warning!", message="You have a big pair of underware in your pants.")
    #messagebox.showerror(title="Oops")
    #if messagebox.ask(title="Ask", message="Do you want to eat cake?"):
    #    print("You ate cake.")
    #else:
    #    print("You left the cake.")
    
    #messagebox.askretrycancel(message="Do you want to try again?")
    #if messagebox.askyesno(message="Do you like cake?"):
    #    print("You're cool.")
    #else:
    #    print("You're lame.")
    #
    answer = messagebox.askquestion(message="Do you think boats are cool?")
    if answer == "yes":
        print("I like boats too.")
    elif answer == "no":
        print("Aww, why not? Boats are cool.")

    secondAnswer = messagebox.askyesnocancel(message="Do you want to eat pie?")
    if secondAnswer:
        print("I'm happy that you'd love to eat some of my famous pie.")
    elif secondAnswer == False:
        print("That's okay, I'm sure I'll find someone else to eat it.")
    else:
        print("What? Where are you going?")

window = Tk()

button = Button(window, command=click, text="Click Me")
button.pack()

window.mainloop()
