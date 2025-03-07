# Author: Chase Quinn
# Date: Refactored on 3/6/2025
# pyCalc Tkinter Root Return Function

import tkinter as tk
import os

def returnRoot():
    root = tk.Tk()
    root.geometry("225x340")
    root.title("pyCalc")
    root.resizable(False, False)
    iconImage = tk.PhotoImage(file=os.getcwd() + "/bin/icon/pyCalcIcon.png")
    root.iconphoto(False, iconImage)
    root.configure(bg="#bdbdbd")
    return root