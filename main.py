import keyboard
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from UI.ui_password import Ui_Dialog
from CreatePassord import *


# from PySide6.QtUiTools import QUiLoader


class MainWindow(Ui_Dialog, QMainWindow, QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.regex = regex
        self.default_radio.setChecked(True)

    def print_default_password(self):
        if self.default_radio.isChecked():
            self.pushButton.clicked.connect(self.createPassword)

    def retrieve_number(self):
        self.nbr = self.char_size.text()

    def retrieve_char(self):
        if self.char_radio.isChecked():
            regex = win.input_char.text()
            print(regex)

    def createPassword(self):
        password = CreatePassword()
        return password.complexPassword()


"""
* Init QUiLoader for other import UI method
    loader = QUiLoader()
    win = loader.load("UI/ui_password.ui", None)
"""

app = QApplication()
win = MainWindow()
win.show()

if __name__ == '__main__':
    keyboard.on_press(lambda input: win.retrieve_char)
    win.print_default_password()
    app.exec()
