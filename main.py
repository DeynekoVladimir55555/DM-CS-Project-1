import init_paths
import sys
#GUI
from PyQt6.QtWidgets import QApplication
from GUI.MainWindow import MainWindow
from GUI.HelpWindow import HelpWindow
from GUI.PolinomWindow import PolinomWindow
#Test
#from src.test.TestModule import test_main
#from src.test.RandomNumbers import generator


def main():
    # GUI
    app = QApplication(sys.argv)
    mw = MainWindow()
    hw = HelpWindow(mw)
    pw = PolinomWindow(mw)
    mw.add_hw_pw(hw, pw)

    mw.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()