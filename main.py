import init_paths
import sys
#GUI
from PyQt6.QtWidgets import QApplication
from GUI.MainWindow import MainWindow
from GUI.HelpWindow import HelpWindow
#Test
#from src.test.TestModule import test_main
#from src.test.RandomNumbers import generator


def main():
    # GUI
    app = QApplication(sys.argv)
    hw = HelpWindow()
    mw = MainWindow(hw)

    mw.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()