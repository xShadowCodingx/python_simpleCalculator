# Main entry point for the calculator

# Global imports
import tkinter as tk
from tkinter import ttk
import os, re, math

# Local module imports
from bin import rootFunc, UIcomponents, functionHandler, config, numberbox, root

# Configure keypress event handler
def handleKeys(event):
    # print(f"Key Pressed: {event.char}")
    if event.char == "1" or event.char == "2" or event.char == "3" or event.char == "4" or event.char == "5" or event.char == "6" or event.char == "7" or event.char == "8" or event.char == "9" or event.char == "0":
        functionHandler.funcHandler.addToBox(event.char)
    if event.char == "*" or event.char == "/" or event.char == "-" or event.char == "+" or event.char == ".":
        functionHandler.funcHandler.addToBox(event.char)
    if event.char == "c" or event.char == "C":
        functionHandler.funcHandler.clear()
    # Otherwise it will ignore it

# Initialize Objects
uiComponents = UIcomponents.UIComponents(root.root, ttk, functionHandler.funcHandler.addToBox, functionHandler.funcHandler.clear, functionHandler.funcHandler.solveEquation)

# Configure UI components
uiComponents.returnOperators()
uiComponents.returnNumberPad()

# Bind keypresses to functions
root.root.bind("<Key>", handleKeys)
root.root.bind("<Return>", lambda event: functionHandler.funcHandler.solveEquation())

# UI Mainloop
root.root.mainloop()