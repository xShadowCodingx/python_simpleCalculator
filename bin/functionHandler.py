# Author: Chase Quinn
# Date: 3/6/2025
# pyCalc Function Handler Class

import re
from . import config, numberbox

class funcHandler:
    def __init__(self):
        pass

    @staticmethod
    def updateTextbox():
        numberbox.numberbox.configure(text=config.currentText)
    
    @staticmethod
    def clear():
        config.currentText = ""
        funcHandler.updateTextbox(numberbox.numberbox)
    
    @staticmethod
    def addToBox(x):
        config.operators = ["+", "-", "*", "/", "²", "%"]
        if config.newEquation == True:
            if x not in config.operators and x != "0":
                config.currentEquation = str(x)
                config.currentText = str(x)
                funcHandler.updateTextbox()
                config.newEquation = False
            else:
                pass
        else:
            splitText = list(config.currentText)
            if len(splitText) == 0:
                if x in config.operators:
                    pass
                else:
                    config.currentText = config.currentText + str(x)
            if len(splitText) > 0:
                if len(splitText) >= 35:
                    print("Long text")
                if len(splitText) == 35 and splitText[0] != "." and splitText[1] != "." and splitText[2] != ".":
                    print("Not concatentated")
                else:
                    print("Short String")
                priorValue = splitText[len(splitText) - 1]
                if x in config.operators and priorValue in config.operators:
                    pass
                else:
                    if x == "\u221a" and priorValue in config.operators:
                        config.currentText = config.currentText + str(x)
                    elif x == "\u221a" and priorValue not in config.operators:
                        pass
                    elif x in config.operators and priorValue not in config.operators:
                        config.currentText = config.currentText + str(x)
                    else:
                        config.currentText = config.currentText + str(x)
            funcHandler.updateTextbox()

    @staticmethod
    def separateEquation():
        return re.findall(r'\d+|[+\-*/%\u221a²]', config.currentText)

    @staticmethod
    def solveEquation():
        listSolution = funcHandler.separateEquation()
        for index, i in enumerate(listSolution):
            if i == "\u221a":
                listSolution[index] = f"math.sqrt({listSolution[index + 1]})"
                listSolution.pop(index + 1)
            if i == "²":
                listSolution[index] = "**2"
        currentEq = "".join(listSolution)
        solution = "=" + str(eval(currentEq))
        config.currentText = solution
        funcHandler.updateTextbox()
        config.newEquation = True