from ast import Expression
from distutils.log import ERROR
import gui_logic
from functools import partial

def evaluateExpression(expression):
        """Evaluate an expression (Model)."""
        try:
            result = str(eval(expression, {}, {}))
        except Exception:
            result = gui_logic.ERROR_MSG
        return result

class PyCalc:
    def __init__(self,model,view) -> None:
        self._evaluate=model;
        self._view=view;
        self._connectSignalAndSlots()
    
    def _calculateResult(self):
        result=self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)
    
    def _buildExpression(self,subExpression):
        if self._view.displayText()==gui_logic.ERROR_MSG:
            self._view.clearDisplay()
        expression=self._view.displayText()+subExpression
        self._view.setDisplayText(expression)

    def _connectSignalAndSlots(self):
        for keySymbol,button in self._view.buttonMap.items():
            if keySymbol!="=" or keySymbol!="C":
                button.clicked.connect(
                    partial(self._buildExpression,keySymbol)
                )
            self._view.buttonMap["="].clicked.connect(self._calculateResult)
            self._view.display.returnPressed.connect(self._calculateResult)
            self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)

def main():
    """PyCalc's main function."""
    pycalcApp = gui_logic.QApplication([])
    pycalcWindow = gui_logic.PyCalcWin()
    pycalcWindow.show()
    PyCalc(model=evaluateExpression, view=pycalcWindow)
    gui_logic.sys.exit(pycalcApp.exec())

if __name__=="__main__":
    main()
