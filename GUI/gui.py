#gui

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from other.gui_fe import Ui_MainWindow




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()



from main import setup

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys_setup = setup(window.ui)


    sys.exit(app.exec())


