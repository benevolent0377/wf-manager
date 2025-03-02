import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

root = tk.Tk()


def compile():
    global root 

    root.title("Warframe Manager - SNAPSHOT 1.0.0")
    root.geometry("650x300")
    root.resizable(0, 0)


    
    # create all of the main containers
    top_frame = tk.Frame(root, bg='cyan', width=650, height=50, pady=3)
    center = tk.Frame(root, bg='gray2', width=50, height=90, padx=3, pady=3)

    # layout all of the main containers
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    top_frame.grid(row=0, sticky="ew")
    center.grid(row=1, sticky="nsew")

    # create the widgets for the top frame
    homeIcon =  packImage("../data/wf-items/data/img/glyphed-clan-sigil-87de90e005.png", 50, 50)
    homeButton = tk.Button(top_frame, image=homeIcon, width = 50, height=50)

    modeDropdown = tk.OptionMenu(top_frame, "Dashboard", *["hello", "bye"])

    timeLabel = tk.Label(top_frame, text="12:12:45 CST", width = 50)

    # layout the widgets in the top frame
    homeButton.grid(row=0, columnspan=1)
    modeDropdown.grid(row=0, column=2, columnspan=3, padx = 10)
    timeLabel.grid(row=0, column=5, sticky="ns", rowspan=2, columnspan=3, padx = 5)
    #entry_W.grid(row=1, column=1)
    #entry_L.grid(row=1, column=3)

    # create the center widgets
    center.grid_rowconfigure(0, weight=1)
    center.grid_columnconfigure(1, weight=1)

    ctr_left = tk.Frame(center, bg='blue', width=100, height=250)
    ctr_mid = tk.Frame(center, bg='yellow', width=250, height=250, padx=3, pady=3)

    ctr_left.grid(row=0, column=0, sticky="ns")
    ctr_mid.grid(row=0, column=1, sticky="nsew")

    root.mainloop()


def menu():
    isAuth = False # assuming the user is a guest, no login functionality has been made yet
    
    rootFrame = Frame(root, bg="yellow", width=650,  height=50, pady = 3).grid(row =0, columnspan = 3)

    if not isAuth:
        print()

def packImage(file, x, y):

    image = ImageTk.PhotoImage(Image.open(file).resize((x, y)))

    return image


def main():
    
    compile()


if __name__ == "__main__":
    main()


