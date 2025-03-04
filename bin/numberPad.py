# Numberpad class

class NPad:
    def __init__(self, root, ttk, addToBox):
        self.root = root
        self.ttk = ttk
        self.addToBox = addToBox

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