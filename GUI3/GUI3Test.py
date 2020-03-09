import sys
import GUI3
from PyQt5.QtWidgets import QApplication, QDialog
if __name__ == '__main__':
  myapp = QApplication(sys.argv)
  myDlg = QDialog()
  myUI = GUI3.Ui_Dialog()
  myUI.setupUi(myDlg)
  myDlg.show()
  sys.exit(myapp.exec_())