from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QFrame, QLabel, QPushButton, QButtonGroup, QTextEdit, \
    QComboBox

from GUI.uis.main_ui import Ui_MainWindow
from src.run import run


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, operations):
        super().__init__()
        self.setupUi(self)
        self.hw = None
        self.pw = None
        self.containers = []
        self.text_edits = []
        self.operations = operations
        self.active_container = None
        self.btn_group = QButtonGroup(self)
        self.btn_group.idClicked.connect(self.call_operation)

        self.main_layout = QHBoxLayout()
        self.centralwidget.setLayout(self.main_layout)
        self.main_layout.addStretch(7)

        self.main_layout.addWidget(self.create_set_nat(), stretch=7)
        self.main_layout.addWidget(self.create_set_int(), stretch=7)
        self.main_layout.addWidget(self.create_set_rat(), stretch=7)
        self.main_layout.addWidget(self.create_set_pol(), stretch=7)

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

    def add_hw_pw(self, hw, pw):
        self.hw = hw
        self.pw = pw
        self.helpButton.clicked.connect(self.hw.show)

    def create_set_nat(self):
        set_nat = QFrame()
        main_lay = QHBoxLayout(set_nat)
        edits = []

        inputs = QHBoxLayout()
        input_names = ["Введите число A", "0", "Введите число B", "0", "Ответ", ""]
        for i in range(0, 6, 2):
            inputs.addWidget(QLabel(input_names[i]))
            te = QTextEdit(input_names[i + 1])
            te.setMaximumHeight(70)
            inputs.addWidget(te)
            edits.append(te)

        btns = QVBoxLayout()
        btn_names = ["A + 1", "B + 1", "A + B", "|A - B|", "A * B", "НОД", "НОК"]
        for i in range(0, 7):
            btn = QPushButton(btn_names[i])
            btns.addWidget(btn)
            self.btn_group.addButton(btn, i)

        main_lay.addLayout(inputs, stretch=6)
        main_lay.addLayout(btns, stretch=1)

        self.containers.append(set_nat)
        self.text_edits.append(edits)
        set_nat.hide()
        return set_nat

    def create_set_int(self):
        set_int = QFrame()
        main_lay = QHBoxLayout(set_int)
        edits = []

        inputs = QHBoxLayout()
        input_names = ["Введите число А", "0", "Введите число В", "0", "Ответ", ""]
        for i in range(0, 6, 2):
            inputs.addWidget(QLabel(input_names[i]))
            if i < 4:
                combo = QComboBox()
                combo.addItems(["+", "-"])
                inputs.addWidget(combo)
            te = QTextEdit(input_names[i + 1])
            te.setMaximumHeight(70)
            inputs.addWidget(te)
            edits.append(te)

        btns = QVBoxLayout()
        btn_names = ["A + B", "A - B", "A * B", "A div B", "A mod B"]
        for i in range(7, 12):
            btn = QPushButton(btn_names[i - 7])
            btns.addWidget(btn)
            self.btn_group.addButton(btn, i)

        main_lay.addLayout(inputs, stretch=6)
        main_lay.addLayout(btns, stretch=1)

        self.containers.append(set_int)
        self.text_edits.append(edits)
        set_int.hide()
        return set_int

    def create_set_rat(self):
        set_rat = QFrame()
        main_lay = QHBoxLayout(set_rat)
        edits = []

        inputs = QHBoxLayout()
        input_names = ["Введите число А", "0", "1", "Введите число В", "0", "1"]
        for i in range(0, 6, 3):
            inputs.addWidget(QLabel(input_names[i]))

            combo = QComboBox()
            combo.addItems(["+", "-"])
            inputs.addWidget(combo)

            v_input = QVBoxLayout()
            v_input.addStretch(5)
            for j in range(1, 3):
                te = QTextEdit(input_names[i + j])
                te.setMaximumHeight(70)
                v_input.addWidget(te)
                edits.append(te)
            v_input.addStretch(5)

            inputs.addLayout(v_input)

        inputs.addWidget(QLabel("Ответ"))
        te = QTextEdit()
        te.setMaximumHeight(70)
        inputs.addWidget(te)

        btns = QVBoxLayout()
        btn_names = ["A + B", "A - B", "A * B", "A / B"]
        for i in range(12, 16):
            btn = QPushButton(btn_names[i - 12])
            btns.addWidget(btn)
            self.btn_group.addButton(btn, i)

        main_lay.addLayout(inputs, stretch=6)
        main_lay.addLayout(btns, stretch=1)

        self.containers.append(set_rat)
        self.text_edits.append(edits)
        set_rat.hide()
        return set_rat

    def create_set_pol(self):
        set_pol = QFrame()
        main_lay = QVBoxLayout(set_pol)
        edits = []



        self.containers.append(set_pol)
        self.text_edits.append(edits)
        set_pol.hide()
        return set_pol

    def call_operation(self, btn_id):
        if btn_id < 7:
            pass

        if btn_id < 12:
            pass

        print("Called", btn_id)

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