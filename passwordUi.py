from PySide6 import QtWidgets
from CreatePassord import *


class App(QtWidgets.QWidget):
    def __int__(self):
        super().__init__()


app = QtWidgets.QApplication([])
win = App()
win.show()

if __name__ == '__main__':
    app.exec_()


