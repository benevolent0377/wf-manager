#a file for the GUI commands
from source.lib import GUI

global app

def init(item):
    global app

    app = item

def viewSelection(item):

    if item.lower() == 'cycle viewer':
        width = 400
        height = 600
    elif item.lower() == 'reliquary':
        width= 700
        height = 500
    elif item.lower() == 'modding':
        width = 1200
        height= 600
    elif item.lower() == 'wiki':
        width = 700
        height = 500
    elif item.lower() == 'weapon lab':
        width = 1200
        height = 600
    elif item.lower() == 'inventory':
        width = 700
        height = 700
    else:
        width = 800
        height = 500

    
    buildPopOut(width, height, f"Warframe Manager - {item}")

def menuSelection(item):
    
    width = 700
    height = 500

    if item.lower() != "close":
        
        buildPopOut(width, height, f"Warframe Manger - {item}")

def accountSelection(item):
    
    if item.lower() == "profile":
        width = 500
        height = 600
    elif item.lower() == 'settings':
        width = 500
        height = 600

    if item.lower() != 'logout':

        buildPopOut(width, height, f"Warframe Manager - {item}")

def search(event=""):
    print(app.mainFrame.searchBox.get())

def autoComplete(item):
    pass

def buildPopOut(width, height, title):

    popOut = GUI.PopOut(width, height, title)
