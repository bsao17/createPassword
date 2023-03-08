from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from UI.ui_password import Ui_Dialog
import keyboard
from CreatePassord import *


# from PySide6.QtUiTools import QUiLoader


class MainWindow(Ui_Dialog, QMainWindow, QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.input_char = ""
        self.setupUi(self)
        title = self.setWindowTitle("Complex Password Lab")
        button = self.buttons
        button.accepted.connect(self.retrieve_number)
        cancel = button.rejected
        cancel.connect(self.apply)

        self.nbr = ""

    def retrieve_number(self):
        print(self.char_size.text)

    def retrieve_char(self):
        regex = self.input_char.text()
        print(regex)

    def reset(self):
        pass

    def apply(self):
        self.retrieve_char()


"""
* Init QUiLoader for other import UI method
    loader = QUiLoader()
    win = loader.load("UI/ui_password.ui", None)
"""

if __name__ == '__main__':
    app = QApplication()
    win = MainWindow()
    win.show()
    keyboard.on_press(lambda a: win.retrieve_char())
    app.exec()
