# Main entry point for the calculator

# Global imports
import tkinter as tk
from tkinter import ttk
import os

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
global currentText, currentEquation
currentText = ""
currentEquation = ""

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
    global currentText
    currentText = currentText + str(x)
    updateTextbox()

def solveEquation():
    global currentText
    updateTextbox()
    print("Solve for: " + currentText)

opButtons = operatorButtons.OpBtn(root, ttk, addToBox, clear, solveEquation)
nPad = numberPad.NPad(root, ttk, addToBox)

# Configure UI components

opButtons.returnButtons()
nPad.returnNumberPad()

root.mainloop()