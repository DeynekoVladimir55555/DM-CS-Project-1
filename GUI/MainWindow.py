from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QFrame, QLabel, QPushButton

from GUI.uis.main_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.hw = None
        self.containers = []
        self.active_container = None

        self.main_layout = QHBoxLayout()
        self.centralwidget.setLayout(self.main_layout)
        self.main_layout.addStretch(6)

        self.main_layout.addWidget(self.create_set_nat(), stretch=6)
        self.main_layout.addWidget(self.create_set_int(), stretch=6)
        self.main_layout.addWidget(self.create_set_rat(), stretch=6)
        self.main_layout.addWidget(self.create_set_pol(), stretch=6)

        self.con_layout = QVBoxLayout()
        self.con_layout.addWidget(self.natButton)
        self.con_layout.addWidget(self.intButton)
        self.con_layout.addWidget(self.ratButton)
        self.con_layout.addWidget(self.polButton)
        self.con_layout.addWidget(self.helpButton)
        self.main_layout.addLayout(self.con_layout, stretch=1)

        self.natButton.clicked.connect(self.nat)
        self.intButton.clicked.connect(self.int)
        self.ratButton.clicked.connect(self.rat)
        self.polButton.clicked.connect(self.pol)

    def add_hw(self, hw):
        self.hw = hw
        self.helpButton.clicked.connect(self.hw.show)

    def create_set_nat(self):
        set_nat = QFrame()
        lay = QVBoxLayout(set_nat)
        lay.addWidget(QLabel("-----set nat-----"))
        self.containers.append(set_nat)
        set_nat.hide()
        return set_nat

    def create_set_int(self):
        set_int = QFrame()
        lay = QVBoxLayout(set_int)
        lay.addWidget(QLabel("-----set int-----"))
        self.containers.append(set_int)
        set_int.hide()
        return set_int

    def create_set_rat(self):
        set_rat = QFrame()
        lay = QVBoxLayout(set_rat)
        lay.addWidget(QLabel("-----set rat-----"))
        self.containers.append(set_rat)
        set_rat.hide()
        return set_rat

    def create_set_pol(self):
        set_pol = QFrame()
        lay = QVBoxLayout(set_pol)
        lay.addWidget(QLabel("-----set pol-----"))
        self.containers.append(set_pol)
        set_pol.hide()
        return set_pol

    def hide_set(self):
        if self.active_container is not None:
            self.active_container.hide()
        else:
            scratch = self.main_layout.takeAt(0)
            del scratch

    def nat(self):
        self.hide_set()
        self.active_container = self.containers[0]
        self.containers[0].show()

    def int(self):
        self.hide_set()
        self.active_container = self.containers[1]
        self.containers[1].show()

    def rat(self):
        self.hide_set()
        self.active_container = self.containers[2]
        self.containers[2].show()

    def pol(self):
        self.hide_set()
        self.active_container = self.containers[3]
        self.containers[3].show()