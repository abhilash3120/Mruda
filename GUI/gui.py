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
from envelope import envelope_set
from update import firmware_update
from ac_scale import autocorr_set
from set_default import set_Default

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys_setup = setup(window.ui)
    env_setup = envelope_set(window.ui)
    update = firmware_update(window.ui)
    ac = autocorr_set(window.ui, sys_setup)
    default = set_Default(window.ui, sys_setup)

    
    sys.exit(app.exec())


