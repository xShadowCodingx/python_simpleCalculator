# Numberbox class

class NBox:
    def __init__(self, root, ttk, currentText):
        self.root = root
        self.ttk = ttk
        self.currentText = currentText
    
    def returnBox(self):
        numberbox = self.ttk.Label(self.root, text=self.currentText, background="#FFFFFF")
        numberbox.place(x=5, y=5, width=215, height=50)