# Main entry point for the calculator

# Local module imports
from bin import UIcomponents, functionHandler, root

# Initialize Objects
uiComponents = UIcomponents.UIComponents(root.root, functionHandler.funcHandler.addToBox, functionHandler.funcHandler.clear,
                                        functionHandler.funcHandler.solveEquation, functionHandler.funcHandler.backSpace)

# Configure UI components
uiComponents.returnOperators()
uiComponents.returnNumberPad()

# Bind keypresses to functions
root.root.bind("<Key>", functionHandler.funcHandler.handleKeys)
root.root.bind("<Return>", lambda event: functionHandler.funcHandler.solveEquation())

# UI Mainloop
root.root.mainloop()