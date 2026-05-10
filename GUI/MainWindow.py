from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, \
    QVBoxLayout, QFrame, QLabel, QPushButton, QButtonGroup, \
    QTextEdit, QComboBox, QTextBrowser

from GUI.uis.main_ui import Ui_MainWindow
from src.run import run
from src.DataClasses.Polinom import Polinom


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.hw = None
        self.pw = None
        self.containers = []
        self.text_edits = []
        self.combos = [[], [], [], []]
        self.active_container = None
        self.pol_list = [Polinom(), Polinom()]
        self.polinoms = [QTextBrowser(), QTextBrowser()]

        self.natCombo = QComboBox()
        self.intCombo = QComboBox()
        self.ratCombo = QComboBox()
        self.polCombo = QComboBox()
        self.create_combo_btns()
        self.runGroup = QButtonGroup()
        self.runGroup.idClicked.connect(self.run_func)

        self.runNat = QPushButton("Выполнить")
        self.runGroup.addButton(self.runNat, 0)
        self.runInt = QPushButton("Выполнить")
        self.runGroup.addButton(self.runInt, 1)
        self.runRat = QPushButton("Выполнить")
        self.runGroup.addButton(self.runRat, 2)
        self.runPol = QPushButton("Выполнить")
        self.runGroup.addButton(self.runPol, 3)


        self.main_layout = QHBoxLayout()
        self.centralwidget.setLayout(self.main_layout)
        self.main_layout.addStretch(7)

        self.add_coef_a = QPushButton("Добавить")
        self.add_coef_b = QPushButton("Добавить")
        self.add_coef_a.clicked.connect(lambda: self.add_to_pol("a"))
        self.add_coef_b.clicked.connect(lambda: self.add_to_pol("b"))

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

    def create_combo_btns(self):
        self.natCombo.addItems([
            "A com B",
            "A != 0",
            "A + 1",
            "A + B",
            "|A - B|",
            "A * d",
            "A * 10^k",
            "A * B",
            "A - B * d",
            "A / B -> d*10^k",
            "A // B",
            "A % B",
            "НОД",
            "НОК"
        ])
        self.intCombo.addItems([
            "abs A",
            "sign A",
            "A * (-1)",
            "nat A -> int",
            "int A -> nat",
            "A + B",
            "A - B",
            "A * B",
            "A // B",
            "A % B"
        ])
        self.ratCombo.addItems([
            "red A",
            "A is int",
            "int A -> rat",
            "rat A -> int",
            "A + B",
            "A - B",
            "A * B",
            "A / B"
        ])
        self.polCombo.addItems([
            "A + B",
            "A - B",
            "A * q",
            "A * x^k",
            "led A",
            "deg A",
            "A(x) -> (c/d) * Q(x)",
            "A * B",
            "A // B",
            "A % B",
            "НОД",
            "A'(x)",
            "A -> A_red"
        ])

    def run_func(self, id):
        func = ""
        data_type = ""
        dataEdits = self.text_edits[id]
        argv = []
        if id == 0:
            func = self.natCombo.currentText()
            data_type = "nat"
        elif id == 1:
            func = self.intCombo.currentText()
            data_type = "int"
        elif id == 2:
            func = self.ratCombo.currentText()
            data_type = "rat"
            print(len(dataEdits))
        elif id == 3:
            func = self.polCombo.currentText()
            for edit in dataEdits:
                argv.append(edit.toPlainText())
            self.run_pol(func, argv)
            return

        for edit in dataEdits[:-1]:
            argv.append(edit.toPlainText())

        argv.append([0 if btn.currentText() == "+" else 1 for btn in self.combos[id]])
        result = run(func, data_type, argv)
        #print(result)

        dataEdits[-1].setPlainText(result)

    def run_pol(self, func, argv):
        #print(self.pol_list)
        run(func, "pol", argv)

    def create_set_nat(self):
        set_nat = QFrame()
        main_lay = QHBoxLayout(set_nat)
        edits = []

        inputs = QVBoxLayout()
        input_names = ["Введите число A", "0", "Введите число B", "0", "Ответ", ""]
        for i in range(0, 4, 2):
            inputs.addStretch(1)
            inputs.addWidget(QLabel(input_names[i]))
            te = QTextEdit(input_names[i + 1])
            te.setMaximumHeight(70)
            inputs.addWidget(te)
            edits.append(te)

        inputs.addStretch(1)
        d_k = QHBoxLayout()
        d_k.addWidget(QLabel("Введите цифру d"))
        te = QTextEdit("0")
        te.setMaximumHeight(30)
        te.setMaximumWidth(100)
        edits.append(te)
        d_k.addWidget(te)
        d_k.addWidget(QLabel("Введите число k"))
        te = QTextEdit("0")
        te.setMaximumHeight(30)
        te.setMaximumWidth(100)
        edits.append(te)
        d_k.addWidget(te)
        inputs.addLayout(d_k)
        inputs.addStretch(1)

        inputs.addWidget(QLabel(input_names[4]))
        te = QTextEdit(input_names[5])
        te.setMaximumHeight(70)
        inputs.addWidget(te)
        edits.append(te)

        btns = QVBoxLayout()
        btns.addWidget(self.natCombo)
        btns.addWidget(self.runNat)

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

        inputs = QVBoxLayout()
        input_names = ["Введите число А", "0", "Введите число В", "0", "Ответ", ""]
        for i in range(0, 6, 2):
            inputs.addStretch(1)
            inputs.addWidget(QLabel(input_names[i]))
            if i < 4:
                combo = QComboBox()
                combo.setMaximumWidth(50)
                combo.addItems(["+", "-"])
                inputs.addWidget(combo)
                self.combos[1].append(combo)
            te = QTextEdit(input_names[i + 1])
            te.setMaximumHeight(70)
            inputs.addWidget(te)
            edits.append(te)

        btns = QVBoxLayout()
        btns.addWidget(self.intCombo)
        btns.addWidget(self.runInt)

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

        inputs = QVBoxLayout()
        input_names = ["Введите число А", "0", "1", "Введите число В", "0", "1"]
        for i in range(0, 6, 3):
            inputs.addStretch(1)
            inputs.addWidget(QLabel(input_names[i]))
            h_input = QHBoxLayout()

            combo = QComboBox()
            combo.setMaximumWidth(50)
            combo.addItems(["+", "-"])
            h_input.addWidget(combo)
            self.combos[2].append(combo)

            v_input = QVBoxLayout()
            v_input.addStretch(5)
            for j in range(1, 3):
                te = QTextEdit(input_names[i + j])
                te.setMaximumHeight(70)
                v_input.addWidget(te)
                edits.append(te)
            h_input.addLayout(v_input)

            inputs.addLayout(h_input)

        inputs.addWidget(QLabel("Ответ"))
        te = QTextEdit()
        te.setMaximumHeight(70)
        inputs.addWidget(te)
        edits.append(te)

        btns = QVBoxLayout()
        btns.addWidget(self.ratCombo)
        btns.addWidget(self.runRat)

        main_lay.addLayout(inputs, stretch=6)
        main_lay.addLayout(btns, stretch=1)

        self.containers.append(set_rat)
        self.text_edits.append(edits)
        set_rat.hide()
        return set_rat

    def create_set_pol(self):
        set_pol = QFrame()
        main_lay = QHBoxLayout(set_pol)
        edits = []

        inputs = QVBoxLayout()
        inputs.addStretch(1)
        input_names = ["Введите коэффициент многочлена А", "Введите коэффициент многочлена B", "X^"]
        for i in range(2):
            inputs.addWidget(QLabel(input_names[i]))
            pol_input = QHBoxLayout()

            combo = QComboBox()
            combo.setMaximumWidth(40)
            combo.addItems(["+", "-"])
            pol_input.addWidget(combo)
            self.combos[3].append(combo)

            edit = QVBoxLayout()
            for j in range(2):
                te = QTextEdit(str(j))
                te.setMaximumHeight(70)
                te.setMaximumWidth(100)
                edit.addWidget(te)
                edits.append(te)
            pol_input.addLayout(edit)

            pol_input.addWidget(QLabel(input_names[2]))
            te = QTextEdit("1")
            te.setMaximumHeight(30)
            te.setMaximumWidth(50)
            edits.append(te)
            pol_input.addWidget(te)
            pol_input.addWidget([self.add_coef_a if i == 0 else self.add_coef_b][0])
            pol_input.addStretch(4)

            inputs.addLayout(pol_input)
            inputs.addStretch(1)

        polinoms = QVBoxLayout()
        polinoms.addStretch(1)
        polinoms.addWidget(self.polinoms[0])
        polinoms.addStretch(1)
        polinoms.addWidget(self.polinoms[1])
        polinoms.addStretch(1)

        btns = QVBoxLayout()
        btns.addWidget(self.polCombo)
        btns.addWidget(self.runPol)

        main_lay.addLayout(inputs)
        main_lay.addLayout(polinoms)
        main_lay.addLayout(btns)

        self.containers.append(set_pol)
        self.text_edits.append(edits)
        set_pol.hide()
        return set_pol

    def add_to_pol(self, which):
        print("added", which)

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