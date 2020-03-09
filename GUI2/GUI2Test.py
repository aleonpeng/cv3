import sys
import GUI2
from PyQt5.QtWidgets import QApplication, QDialog
if __name__ == '__main__':
  myapp = QApplication(sys.argv)
  myDlg = QDialog()
  myUI = GUI2.Ui_Dialog()
  myUI.setupUi(myDlg)
  myDlg.show()
  sys.exit(myapp.exec_())