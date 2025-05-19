import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter import font
from source.core import system
from PIL import Image, ImageTk
from source.lib import interfaceCmd as cmd

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.width = 550
        self.height = 55

        self.title("Warframe Manager")
        self.geometry(f'{str(self.width)}x{str(self.height)}+0+0')
        self.resizable(False, False)

        cmd.init(self)


    class mainFrame(tk.Frame):
        def __init__(self, container):
            super().__init__(container)

            self.columnconfigure(0, weight= 1)
            self.columnconfigure(2, weight=1)
            self.columnconfigure(6, weight=3)
            self.rowconfigure(0, weight =1)
            self.initButtonTray()

        def initButtonTray(self):

            self.menuFont = font.Font(family="Arial", size=12)

            self.menuIcon = packImage(f"{system.getCWD()}/source/sysimg/icons/menu-button.png", 50, 40)
            self.accountIcon = packImage(f"{system.getCWD()}/source/sysimg/icons/account.png", 50, 50)
            self.searchImg = packImage(f"{system.getCWD()}/source/sysimg/icons/search.png", 20, 20)

            # menu button
            self.menuText = tk.StringVar(value="")
            self.menuItems = ['Home', 'Lorem', 'Ipsum', 'Solom', 'Dor', 'Omet', 'Close']
            self.menuBtn = tk.OptionMenu(self, self.menuText, *self.menuItems, command=cmd.menuSelection)
            self.menuBtn.config(height=50, width=60, font=self.menuFont, image=self.menuIcon, indicatoron=0)
            
            # view button
            self.viewText = tk.StringVar(value="Mode Selection")
            self.modes = ["Cycle Viewer", "Reliquary", "Modding", "Wiki", "Weapon Lab", "Inventory"]
            self.viewBtn = tk.OptionMenu(self, self.viewText, *self.modes, command=cmd.viewSelection)
            self.viewBtn.config(width=12, height=50, font=self.menuFont)
            
            #self.spacer = tk.Label(self, width=47, bg="#aaaaaa")

            #making the search bar
            self.searchContainer = tk.Frame(self, bg='#aaaaaa')
            self.searchContainer.columnconfigure(0, weight=2)

            self.searchText = tk.StringVar()
            self.searchBox = ttk.Entry(self.searchContainer, textvariable=self.searchText, font=("Arial", 12))
            self.suggestions = tk.Listbox(self.searchContainer, font=self.menuFont)
            self.searchButton = tk.Button(self.searchContainer, image=self.searchImg, width=20, height=20, font=("Arial", 12), command=cmd.search)

            self.searchBox.pack(side="left", expand=True)
            self.searchButton.pack(side="right")
            self.searchBox.bind('<Return>', cmd.search)
            
            # account button
            self.accountText = tk.StringVar(value="")
            self.accountOptions = ["Profile", "Settings", "Log Out"]
            self.accountBtn = tk.OptionMenu(self, self.accountText, *self.accountOptions, command= cmd.accountSelection)
            self.accountBtn.config(height=50, width=60, font=self.menuFont, image = self.accountIcon, indicatoron=0)

            self.menuBtn.grid(row=0, column=0, padx=0,pady=1, sticky="W")
            self.viewBtn.grid(row=0, column =2, padx=7, pady=1)
            self.searchContainer.grid(row=0, column=4, padx=8)
            self.accountBtn.grid(row=0, column=6, padx=0, pady=1, sticky="E")
            

    def framePack(self):
        self.mainFrame = self.mainFrame(self)
        self.mainFrame.config(bg="#aaaaaa", width=self.width, height=self.height)
        self.mainFrame.pack(expand=True, fill=tk.X)


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
