import sys
import WinGet
from PyQt5.QtWidgets import QApplication, QDialog, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets

def display_count(self, Form):
    for i in (1,100):
        WinGet


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = QWidget()
    myUI = WinGet.Ui_Form()
    myUI.setupUi(myWin)
    myWin.show()
    sys.exit(app.exec_())