#a file for the GUI commands
from source.lib.GUI import PopOut

global app

def init(item):
    global app

    app = item

def viewSelection(item):
    print(item)

def menuSelection(item):
    print(item)

def accountSelection(item):
    print(item)

def search(event=""):
    print(app.mainFrame.searchBox.get())

def autoComplete(item):
    pass
