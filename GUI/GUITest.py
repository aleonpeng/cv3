import sys
import GUI
from PyQt5.QtWidgets import QApplication, QDialog

from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QDialog,QMessageBox

if __name__ == '__main__':
  myapp = QApplication(sys.argv)
  myDlg = QDialog()
  myUI = GUI.Ui_MainWindow()
  myUI.setupUi(myDlg)
  myDlg.show()
  sys.exit(myapp.exec_())