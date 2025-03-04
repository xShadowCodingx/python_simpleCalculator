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

# Configure Current Textbox String
currentText = ""
currentEquation = ""

# Configure Text Operations for Textbox String
def clear(currentText):
    currentText = ""
    print(currentText)

def addToBox(currentText, x):
    currentText = currentText + str(x)
    print(currentText)

# Object initializations
opButtons = operatorButtons.OpBtn(root, ttk)
nBox = numberBox.NBox(root, ttk, currentText)
nPad = numberPad.NPad(root, ttk)

# Configure UI components
nBox.returnBox()
opButtons.returnButtons()
nPad.returnNumberPad()

root.mainloop()