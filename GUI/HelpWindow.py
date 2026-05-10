from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from GUI.uis.help_ui import Ui_Help


class HelpWindow(QWidget, Ui_Help):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Справка")
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowStaysOnTopHint)

        self.closeButton.clicked.connect(self.close)

    def set_text(self, text):
        self.helpBrowser.setText()