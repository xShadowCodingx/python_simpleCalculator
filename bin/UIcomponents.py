# Author: Chase Quinn
# Date: Refactored on 3/6/2025
# pyCalc UI Components Class

import tkinter as ttk

class UIComponents:
    def __init__(self, root, addToBox, clear, solveEquation, backspace):
        self.root = root
        self.ttk = ttk
        self.addToBox = addToBox
        self.clear = clear
        self.solveEquation = solveEquation
        self.backspace = backspace
    
    @staticmethod
    def returnNumberBox(root):
        numberbox = ttk.Label(root, text="", background="#FFFFFF", relief="sunken")
        numberbox.place(x=5, y=5, width=215, height=50)
        return numberbox

    def returnNumberPad(self):
        sevenButton = self.ttk.Button(self.root, text="7", command=lambda : self.addToBox(7))
        sevenButton.place(x=5, y=120, height=50, width=50)
        eightButton = self.ttk.Button(self.root, text="8", command=lambda : self.addToBox(8))
        eightButton.place(x=60, y=120, height=50, width=50)
        nineButton = self.ttk.Button(self.root, text="9", command=lambda : self.addToBox(9))
        nineButton.place(x=115, y=120, height=50, width=50)
        fourButton = self.ttk.Button(self.root, text="4", command=lambda : self.addToBox(4))
        fourButton.place(x=5, y=175, height=50, width=50)
        fiveButton = self.ttk.Button(self.root, text="5", command=lambda : self.addToBox(5))
        fiveButton.place(x=60, y=175, height=50, width=50)
        sixButton = self.ttk.Button(self.root, text="6", command=lambda : self.addToBox(6))
        sixButton.place(x=115, y=175, height=50, width=50)
        oneButton = self.ttk.Button(self.root, text="1", command=lambda : self.addToBox(1))
        oneButton.place(x=5, y=230, height=50, width=50)
        twoButton = self.ttk.Button(self.root, text="2", command=lambda : self.addToBox(2))
        twoButton.place(x=60, y=230, height=50, width=50)
        threeButton = self.ttk.Button(self.root, text="3", command=lambda : self.addToBox(3))
        threeButton.place(x=115, y=230, height=50, width=50)
        zeroButton = self.ttk.Button(self.root, text="0", command=lambda : self.addToBox(0))
        zeroButton.place(x=60, y=285, height=50, width=50)
    
    def returnOperators(self):
        additionButton = self.ttk.Button(self.root, text="+", command=lambda : self.addToBox("+"))
        additionButton.place(x=5, y=65, height=50, width=50)
        subtractionButton = self.ttk.Button(self.root, text="-", command=lambda : self.addToBox("-"))
        subtractionButton.place(x=60, y=65, height=50, width=50)
        multiplyButton = self.ttk.Button(self.root, text="*", command=lambda : self.addToBox("*"))
        multiplyButton.place(x=115, y=65, height=50, width=50)
        divideButton = self.ttk.Button(self.root, text="/", command=lambda : self.addToBox("/"))
        divideButton.place(x=170, y=65, height=50, width=50)
        squareRootButton = self.ttk.Button(self.root, text="\u221A", command=lambda : self.addToBox("\u221A"))
        squareRootButton.place(x=170, y=120, height=50, width=50)
        moduloButton = self.ttk.Button(self.root, text="%", command=lambda : self.addToBox("%"))
        moduloButton.place(x=170, y=175, height=50, width=50)
        squareButton = self.ttk.Button(self.root, text="x²", command=lambda : self.addToBox("²"))
        squareButton.place(x=170, y=230, height=50, width=50)
        equalsButton = self.ttk.Button(self.root, text="=", command=lambda : self.solveEquation())
        equalsButton.place(x=170, y=285, height=50, width=50)
        clearButton = self.ttk.Button(self.root, text="C", command=lambda : self.clear())
        clearButton.place(x=5, y=285, height=50, width=50)
        backspaceButton = self.ttk.Button(self.root, text="←", command=lambda : self.backspace())
        backspaceButton.place(x=115, y=285, height=50, width=50)