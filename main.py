# Main entry point for the calculator

# Global imports
import tkinter as tk
from tkinter import ttk
import os, re

# Local module imports
from bin import operatorButtons, numberBox, numberPad

# Configure root
root = tk.Tk()
root.geometry("225x340")
root.title("pyCalc")
root.resizable(False, False)
iconImage = tk.PhotoImage(file=os.getcwd() + "/bin/icon/pyCalcIcon.png")
root.iconphoto(False, iconImage)
root.configure(bg="#bdbdbd")

# Configure global variables
global currentText
currentText = ""

global currentEquation
currentEquation = ""

global newEquation
newEquation = False

# Configure number box
numberbox = ttk.Label(root, text="", background="#FFFFFF")
numberbox.place(x=5, y=5, width=215, height=50)

# Configure Text Operations for Textbox String
def updateTextbox():
    global currentText
    numberbox.configure(text=currentText)

def clear():
    global currentText
    currentText = ""
    updateTextbox()

def addToBox(x):
    global newEquation
    global currentText
    if newEquation == True:
        currentText = str(x)
        updateTextbox()
        newEquation = False
    else:
        currentText = currentText + str(x)
        updateTextbox()

def separateEquation():
    global currentText
    return re.findall(r'\d+|[+\-*/%\u221A²]', currentText)

def solveEquation():
    global currentText
    global newEquation
    solution = "=" + str(eval(currentText))
    currentText = solution
    updateTextbox()
    newEquation = True

    # Configure keypress event handler
def handleKeys(event):
    # print(f"Key Pressed: {event.char}")
    if event.char == "1" or event.char == "2" or event.char == "3" or event.char == "4" or event.char == "5" or event.char == "6" or event.char == "7" or event.char == "8" or event.char == "9" or event.char == "0":
        addToBox(event.char)
    if event.char == "*" or event.char == "/" or event.char == "-" or event.char == "+" or event.char == ".":
        addToBox(event.char)
    # Otherwise it will ignore it

# Initialize Objects
opButtons = operatorButtons.OpBtn(root, ttk, addToBox, clear, solveEquation)
nPad = numberPad.NPad(root, ttk, addToBox)

# Configure UI components
opButtons.returnButtons()
nPad.returnNumberPad()

# Bind keypresses to functions
root.bind("<Key>", handleKeys)
root.bind("<Return>", lambda event: solveEquation())

root.mainloop()