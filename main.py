
import keyboard
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from UI.ui_password import Ui_Dialog
from CreatePassord import *


# from PySide6.QtUiTools import QUiLoader


class MainWindow(Ui_Dialog, QMainWindow, QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Complex Password Lab")
        self.setupUi(self)
        self.regex = regex
        self.default_radio.setChecked(True)
        self.pushButton.clicked.connect(self.print_default_password)

    def print_default_password(self):
        password = self.createPassword()
        self.password_display.setPlainText(password)

    def clear_password(self):
        self.password_display.clear()

    def retrieve_char(self):
        if self.char_radio.isChecked():
            regex = self.input_char.text()
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
    win.pushButton_2.clicked.connect(win.clear_password())
    app.exec()
