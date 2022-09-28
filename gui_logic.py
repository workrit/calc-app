import sys
from functools import partial
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QLineEdit,
                             QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QMainWindow, QGridLayout)

# 240 * 240 layout
WINDOW_SIZE = 500
# ERROR_MSG="INVALID EXPRESSION"

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
        self.display.setFixedHeight(65)
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
                self.buttonMap[key].setFixedSize(90, 90)
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
    



    

# def main():
#     """PyCalc's main function."""
#     pycalcApp = QApplication([])
#     pycalcWindow = PyCalcWin()
#     pycalcWindow.show()
#     # print(pycalcWindow.)
#     PyCalc(model=evaluateExpression, view=pycalcWindow)
#     sys.exit(pycalcApp.exec())


# if __name__ == "__main__":
#     main()
