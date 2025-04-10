import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

class mainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.text = ttk.Label(self, text="Test")
        self.text.pack()
        self.pack()

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Warframe Manager")
        self.geometry('300x70')
        self.resizable(False, False)

if __name__ == "__main__":
    app = App()

    mainFrame(app)

    app.mainloop()

