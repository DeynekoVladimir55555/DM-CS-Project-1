import init_paths
import sys
#GUI
from PyQt6.QtWidgets import QApplication
from GUI.MainWindow import MainWindow
from GUI.HelpWindow import HelpWindow
#Objects
from src.DataClasses.NaturalNumber import NaturalNumber
from src.DataClasses.IntNumber import IntNumber
from src.DataClasses.RationalNumber import RationalNumber
from src.DataClasses.Polinom import Polinom
#Test
from src.test.TestModule import test_main
from src.test.RandomNumbers import generator


def main():
    # GUI
    app = QApplication(sys.argv)
    mw = MainWindow()
    hw = HelpWindow()

    mw.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()