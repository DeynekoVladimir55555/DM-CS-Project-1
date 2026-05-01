from PyQt6.QtWidgets import QWidget
from PyQt6.uic import loadUi


class HelpWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("GUI/uis/HelpWindow.ui", self)

        self.closeButton.clicked.connect(self.close)
