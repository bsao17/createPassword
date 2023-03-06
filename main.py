from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from UI.ui_password import Ui_Dialog
from CreatePassord import *
# from PySide6.QtUiTools import QUiLoader


class MainWindow(Ui_Dialog, QMainWindow, QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.nbr = ""
        char = ""

    def retrieve_number(self):
        self.nbr = self.char_size.text()

    def retrieve_char(self):
        regex = self.input_char.text()


"""
* Init QUiLoader for other import UI method
    loader = QUiLoader()
    win = loader.load("UI/ui_password.ui", None)
"""


app = QApplication()
win = MainWindow()
win.show()

if __name__ == '__main__':
    app.exec()
