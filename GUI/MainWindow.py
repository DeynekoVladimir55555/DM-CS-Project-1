from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
from PyQt6.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self, hw):
        self.hw = hw
        super().__init__()
        loadUi("GUI/uis/MainWindow.ui", self)

        self.natButton.clicked.connect(self.nat)
        self.intButton.clicked.connect(self.int)
        self.ratButton.clicked.connect(self.rat)
        self.polButton.clicked.connect(self.pol)
        self.helpButton.clicked.connect(self.help)

    def nat(self):
        print("nat")

    def int(self):
        print("int")

    def rat(self):
        print("rat")

    def pol(self):
        print("pol")

    def help(self):
        self.hw.show()