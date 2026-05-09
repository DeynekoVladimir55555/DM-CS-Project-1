import init_paths
import sys
#GUI
from PyQt6.QtWidgets import QApplication
from GUI.MainWindow import MainWindow
from GUI.HelpWindow import HelpWindow
from GUI.PolinomWindow import PolinomWindow
#Test
from src.test.TestModule import test_main, get_operations
from src.test.RandomNumbers import generator


def main(test = False):
    if test:
        test_main()
        return
    # GUI
    app = QApplication(sys.argv)
    mw = MainWindow(get_operations())
    hw = HelpWindow(mw)
    pw = PolinomWindow(mw)
    mw.add_hw_pw(hw, pw)

    mw.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()