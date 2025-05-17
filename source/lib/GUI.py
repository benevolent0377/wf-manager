import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter import font
from source.core import system
from PIL import Image, ImageTk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.width = 550
        self.height = 55

        self.title("Warframe Manager")
        self.geometry(f'{str(self.width)}x{str(self.height)}')
        self.resizable(True, True)


    class mainFrame(tk.Frame):
        def __init__(self, container):
            super().__init__(container)

            self.columnconfigure(0, weight= 1)
            self.columnconfigure(2, weight=1)
            self.columnconfigure(6, weight=3)
            self.rowconfigure(0, weight =1)
            self.initButtonTray()


        def initButtonTray(self):

            self.menuFont = font.Font(size = 12)

            self.menuIcon = packImage(f"{system.getCWD()}/source/sysimg/icons/menu-button.png", 50, 50)
            self.accountIcon = packImage(f"{system.getCWD()}/source/sysimg/icons/account.png", 50, 50)

            self.menuBtn = tk.Button(self, text="Menu", height=50, font=self.menuFont, image=self.menuIcon)
            self.viewBtn = tk.Button(self, text="View", width=7, height=50, font=self.menuFont)
            self.spacer = tk.Label(self, width=47, bg="#aaaaaa")
            self.accountBtn = tk.Button(self, text="Account", height=50, font=self.menuFont, image = self.accountIcon)

            self.menuBtn.grid(row=0, column=0, padx=5,pady=1, sticky="W")
            self.viewBtn.grid(row=0, column =2, padx=7, pady=1)
            self.spacer.grid(row=0, column=4)
            self.accountBtn.grid(row=0, column=6, padx=5, pady=1, sticky="E")


    def framePack(self):
        self.mainFrame = self.mainFrame(self)
        self.mainFrame.config(bg="#aaaaaa", width=self.width, height=self.height)
        self.mainFrame.pack()

class PopOut(tk.Toplevel):
    def __init__(self, height, width, title):
        super().__init__()

        self.width = width
        self.height = height
        self.title = title


def packImage(file, x, y):

    image = ImageTk.PhotoImage(Image.open(file).resize((x, y)))

    return image


def main():
    app = App()

    app.framePack()

    app.mainloop()

if __name__ == "__main__":
    main()
