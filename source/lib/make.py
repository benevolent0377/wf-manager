import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import cmd

root = tk.Tk()

def MainWindow(version, dimensions):
    global root

    root.title("Warframe Manager - " + version)
    root.geometry(dimensions)
    root.resizable(0,0)

def compile():
    global root
    
    # create all of the main containers
    top_frame = addElement("Frame", root, {"bg": "cyan", "width": "650", "height": "75", "pady": "3"})
    center = addElement("Frame", root, {"bg":'gray2', "width":"50", "height":"90", "padx":"3", "pady":"3"})

    # layout all of the main containers
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    top_frame.grid(row=0, sticky="ew")
    center.grid(row=1, sticky="nsew")

    # create the widgets for the top frame
    #homeIcon =  packImage("../data/wf-items/data/img/glyphed-clan-sigil-87de90e005.png", 50, 50)
    homeButton = addElement("Button", top_frame, {"width": "50", "height":"50"})

    modeDropdown = tk.OptionMenu(top_frame, "Dashboard", *["hello", "bye"])

    #timeLabel = tk.Label(top_frame, text="12:12:45 CST", width = 50)

    timeLabel = addElement("label", top_frame, {'text': "12:12:45 CST", 'width': 50})

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

    testPicture = packImage("../data/wf-items/data/img/6ixgatsu-glyph-fd8eb7ed1f.png", 50, 50)
    testImageObj = tk.Label(ctr_mid, image= testPicture)
    testImageObj.pack()


def menu():
    isAuth = False # assuming the user is a guest, no login functionality has been made yet
    
    rootFrame = Frame(root, bg="yellow", width=650,  height=50, pady = 3).grid(row =0, columnspan = 3)

    if not isAuth:
        print()

def dashboard():
    print()

# place other build functions here too


def newWindow(configOptions, root = False):
    if not root:
        element = tk.Toplevel()
    else:
        element = tk.Tk()

    configArgs = sorted(list(element.configure().keys()))
    optsKeys = list(configOptions.keys())
    checkedIndex = 0
    for item in range(len(configOptions)):
        highEnd = int(len(configArgs)-1)
        lowEnd = 0
        middle = int(highEnd/2)
        #print(optsKeys, "...", configArgs)
        while (optsKeys[item] != configArgs[middle]):

    
            if ord(optsKeys[item][checkedIndex]) > ord(configArgs[middle][checkedIndex]):
                if checkedIndex > 0:
                    checkedIndex = 0
                lowEnd = middle
                if middle == int(middle + (highEnd - middle)/2):
                    middle = int(middle + (highEnd - middle))
                else:
                    middle = int(middle + (highEnd - middle)//2)
                #print(optsKeys[item][checkedIndex], configArgs[middle][checkedIndex])
                #print(f"{middle} + (({highEnd} - {middle})/2)")
        
            elif ord(optsKeys[item][checkedIndex]) < ord(configArgs[middle][checkedIndex]):
                if checkedIndex > 0:
                    checkedIndex = 0
                highEnd = middle
                middle = int((highEnd - lowEnd)/2)
                #print(middle, highEnd)
                #print("lesser")
            else:
                #print(f"{optsKeys[item][checkedIndex]} and {configArgs[middle][checkedIndex]} are the same.")
                if checkedIndex < min(len(optsKeys[item])-1, len(configArgs[middle])-1):
                    checkedIndex = checkedIndex + 1
                elif (optsKeys[item] != configArgs[middle]):
                    break
        
        element[configArgs[middle]] = configOptions[optsKeys[item]]
    
    

    return element

def addElement(elementName, anchor, configOptions):

    elementName = elementName.title()
    match elementName:
        case "Button":
            element = tk.Button(anchor)
        case "Label":
            element = tk.Label(anchor)
        case "Checkbutton":
            element = tk.Checkbutton(anchor)
        case "Radiobutton":
            element = tk.Radiobutton(anchor)
        case "Frame":
            element = tk.Frame(anchor)
        case "Menu":
            element = tk.Menu(anchor)
        case "Menubutton":
            element = tk.Menubutton(anchor)
        case "Entry":
            element = tk.Entry(anchor)
        case "Text":
            element = tk.Text(anchor)
        case "ListBox":
            element = tk.ListBox(anchor)
        case "ComboBox":
            element = tk.ComboBox(anchor)
        case "Scale":
            element = tk.Scale(anchor)
        case "ScrollBar":
            element = tk.ScrollBar(anchor)
        case "Message":
            element = tk.Message(anchor)
        case "Separator":
            element = tk.Separator(anchor)
        case "ProgressBar":
            element = tk.ProgressBar(anchor)
    


    configArgs = sorted(list(element.configure().keys()))
    optsKeys = list(configOptions.keys())
    checkedIndex = 0
    for item in range(len(configOptions)):
        highEnd = int(len(configArgs)-1)
        lowEnd = 0
        #middle = int(highEnd/2)
        middle = 0
        loopCounter = 0
        #print(optsKeys, "...", configArgs)
        while (lowEnd <= highEnd):
            
            if (middle == (highEnd + lowEnd)//2):
                loopCounter +=1

                if loopCounter == 5:
                    break

            middle = (highEnd + lowEnd)//2
    
            if ord(optsKeys[item][checkedIndex]) > ord(configArgs[middle][checkedIndex]):
                
                lowEnd = middle - 1

                #print(optsKeys[item][checkedIndex], configArgs[middle][checkedIndex])
                #print(f"{middle} + (({highEnd} - {middle})/2)")
        
            elif ord(optsKeys[item][checkedIndex]) < ord(configArgs[middle][checkedIndex]):
                
                highEnd = middle + 1

                #print(middle, highEnd)
                #print("lesser")
            else:
                #print(f"{optsKeys[item][checkedIndex]} and {configArgs[middle][checkedIndex]} are the same.")
                element[configArgs[middle]] = configOptions[optsKeys[item]]
    
    

    return element
def main():
    global root
    MainWindow("SNAPSHOT 1.0.0", "650x300")
    compile()
    
    root.mainloop()

if __name__ == "__main__":
    main()


