# Main entry point for the calculator

# Global imports
import tkinter as tk
from tkinter import ttk
import os, re, math

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
global numberbox
numberbox = ttk.Label(root, text="", background="#FFFFFF")
numberbox.place(x=5, y=5, width=215, height=50)

# Configure Text Operations for Textbox String
def updateTextbox():
    global currentText
    global numberbox
    numberbox.configure(text=currentText)

def clear():
    global currentText
    global newEquation
    currentText = ""
    updateTextbox()
    newEquation = True

def addToBox(x):
    global newEquation
    global currentText
    operators = ["+", "-", "*", "/", "²"]
    if newEquation == True:
        if x not in operators:
            currentText = str(x)
            updateTextbox()
            newEquation = False
        else:
            pass
    else:
        splitText = list(currentText)
        if len(splitText) == 0:
            if x in operators:
                pass
            else:
                currentText = currentText + str(x)
        if len(splitText) > 0:
            priorValue = splitText[len(splitText) - 1]
            if x in operators and priorValue in operators:
                pass
            else:
                if x == "\u221a" and priorValue in operators:
                    currentText = currentText + str(x)
                elif x == "\u221a" and priorValue not in operators:
                    pass
                elif x in operators and priorValue not in operators:
                    currentText = currentText + str(x)
                else:
                    currentText = currentText + str(x)
        # currentText = currentText + str(x)
        updateTextbox()

def separateEquation():
    global currentText
    return re.findall(r'\d+|[+\-*/%\u221a²]', currentText)

def solveEquation():
    global currentText
    global newEquation
    listSolution = separateEquation()
    for index, i in enumerate(listSolution):
        if i == "\u221a":
            listSolution[index] = f"math.sqrt({listSolution[index + 1]})"
            listSolution.pop(index + 1)
        if i == "²":
            listSolution[index] = "**2"
    currentEq = "".join(listSolution)
    solution = "=" + str(eval(currentEq))
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
    if event.char == "c" or event.char == "C":
        clear()
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