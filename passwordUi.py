from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader
from CreatePassord import *

loader = QUiLoader()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Complex Password")


app = QApplication()
win = loader.load("UI/ui_password.ui", None)
win.show()
app.exec()
