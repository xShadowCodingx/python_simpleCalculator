# Calculator Operator Buttons class
# 
# This file handles the operator buttons and their functions
# 

class OpBtn:
    def __init__(self, root, ttk, addToBox, clear, solveEquation):
        self.root = root
        self.ttk = ttk
        self.addToBox = addToBox
        self.clear = clear
        self.solveEquation = solveEquation

    def returnButtons(self):
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
        squareButton = self.ttk.Button(self.root, text="x²", command=lambda : self.addToBox("x²"))
        squareButton.place(x=170, y=230, height=50, width=50)
        equalsButton = self.ttk.Button(self.root, text="=", command=lambda : self.solveEquation())
        equalsButton.place(x=170, y=285, height=50, width=50)
        clearButton = self.ttk.Button(self.root, text="C", command=lambda : self.clear())
        clearButton.place(x=5, y=285, height=50, width=50)