from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from UI.ui_password import Ui_Dialog
from CreatePassord import *
# from PySide6.QtUiTools import QUiLoader


class MainWindow(Ui_Dialog, QMainWindow, QDialog):
    def __init__(self):
        super(MainWindow, self).__init__(parent=None)
        self.setupUi(self)
        button = self.buttons
        button.clicked.connect(self.retrieve_number)


        self.nbr = ""
        char = ""

    def retrieve_number(self):
        self.nbr = self.char_size.text()
        print(self.nbr)

    def retrieve_char(self):
        print(self.input_char)

    def reset(self):
        self.input_char = ""

    def apply(self):
        print("apply Ok")


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

