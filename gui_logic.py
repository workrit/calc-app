import sys
from functools import partial
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QLineEdit,
                             QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QMainWindow, QGridLayout)

# 240 * 240 layout
WINDOW_SIZE = 235
ERROR_MSG="INVALID EXPRESSION"

class PyCalcWin(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("CALCULATOR-BY_RIT")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttonMap = {}
        buttonLayout = QGridLayout()
        keyBoard = []
        a = ["7", "8", "9", "/", "C"]
        b = ["4", "5", "6", "*", "("]
        c = ["1", "2", "3", "-", ")"]
        d = ["0", "00", ".", "+", "="]
        keyBoard.append(a)
        keyBoard.append(b)
        keyBoard.append(c)
        keyBoard.append(d)
        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(40, 40)
                buttonLayout.addWidget(self.buttonMap[key], row, col)
        self.generalLayout.addLayout(buttonLayout)

    def setDisplayText(self, text):
        """Set the display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get the display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText("")
    


class PyCalc:
    def __init__(self,model,view) -> None:
        self._evaluate=model;
        self._view=view
        self._connectSignalAndSlots()
    
    def _calculateResult(self):
        result=self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)
    
    def _buildExpression(self,subExpression):
        if self._view.displayText()==ERROR_MSG:
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

def evaluateExpression(expression):
        """Evaluate an expression (Model)."""
        try:
            print(expression)
            result = str(eval(expression, {}, {}))
        except Exception:
            
            result = ERROR_MSG
        return result   

    

def main():
    """PyCalc's main function."""
    pycalcApp = QApplication([])
    pycalcWindow = PyCalcWin()
    pycalcWindow.show()
    PyCalc(model=evaluateExpression, view=pycalcWindow)
    sys.exit(pycalcApp.exec())


if __name__ == "__main__":
    main()
