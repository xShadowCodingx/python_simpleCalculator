# Main entry point for the calculator

# Global imports
from tkinter import *
from tkinter import ttk

# Configure root
root = Tk()
root.geometry("225x340")
root.resizable = False
root.title("pyCalc")

# Configure UI components

# Numberbox
numberbox = ttk.Label(root, text="NONE", background="grey")
numberbox.place(x=5, y=5, width=215, height=50)

# Operator buttons
additionButton = ttk.Button(root, text="+")
additionButton.place(x=5, y=65, height=50, width=50)
subtractionButton = ttk.Button(root, text="-")
subtractionButton.place(x=60, y=65, height=50, width=50)
multiplyButton = ttk.Button(root, text="*")
multiplyButton.place(x=115, y=65, height=50, width=50)
divideButton = ttk.Button(root, text="/")
divideButton.place(x=170, y=65, height=50, width=50)
squareRootButton = ttk.Button(root, text="\u221A")
squareRootButton.place(x=170, y=120, height=50, width=50)
moduloButton = ttk.Button(root, text="%")
moduloButton.place(x=170, y=175, height=50, width=50)
squareButton = ttk.Button(root, text="x²")
squareButton.place(x=170, y=230, height=50, width=50)
equalsButton = ttk.Button(root, text="=")
equalsButton.place(x=170, y=285, height=50, width=50)

# Numberpad buttons
sevenButton = ttk.Button(root, text="7")
sevenButton.place(x=5, y=120, height=50, width=50)
eightButton = ttk.Button(root, text="8")
eightButton.place(x=60, y=120, height=50, width=50)
nineButton = ttk.Button(root, text="9")
nineButton.place(x=115, y=120, height=50, width=50)
fourButton = ttk.Button(root, text="4")
fourButton.place(x=5, y=175, height=50, width=50)
fiveButton = ttk.Button(root, text="5")
fiveButton.place(x=60, y=175, height=50, width=50)
sixButton = ttk.Button(root, text="6")
sixButton.place(x=115, y=175, height=50, width=50)
oneButton = ttk.Button(root, text="1")
oneButton.place(x=5, y=230, height=50, width=50)
twoButton = ttk.Button(root, text="2")
twoButton.place(x=60, y=230, height=50, width=50)
threeButton = ttk.Button(root, text="3")
threeButton.place(x=115, y=230, height=50, width=50)
zeroButton = ttk.Button(root, text="0")
zeroButton.place(x=60, y=285, height=50, width=50)

root.mainloop()