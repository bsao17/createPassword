from PySide6.QtWidgets import QApplication, QWidget
from CreatePassord import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Complex Password")
        self.setFixedSize(600, 200)


app = QApplication()
win = MainWindow()
win.show()
app.exec()
