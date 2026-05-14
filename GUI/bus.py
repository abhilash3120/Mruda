from PySide6.QtCore import Signal, QObject

class Mrida_signal():
    recived_data = Signal(list)
    tx_data = Signal(list)
    