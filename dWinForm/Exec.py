#-*-coding:utf-8-*-

import sys
import dWinForm
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from dWinForm import Ui_MainWindow
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
from PyQt5.QtCore import *

class  RunWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(RunWindow,self).__init__(parent)

        self.setupUi(self)

        self.actionExit.triggered.connect(self.click_exit)

        self.timer_cam = QTimer()
        self.cap = cv2.VideoCapture()

        self.btn_initcam.clicked.connect(self.init_cam_click)
        self.timer_cam.timeout.connect(self.play_vedio)

    def click_exit(self):
        #QMessageBox.information(self,'Warning','Quit!!!')
        myWin.close()
        #sys.exit(app.exec_())

    def play_vedio(self):
        flag, self.image = self.cap.read()
        show = cv2.resize(self.image, (640, 480))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(showImage).scaled(self.lbl_displayImage.width(), self.lbl_displayImage.height())
        self.lbl_displayImage.setPixmap(pixmap)


    def init_cam_click(self):
        try:
            if self.timer_cam.isActive() == False:
                #print(self.cap)
                flag = self.cap.open(0)
                if flag == False:
                    msg = QtWidgets.QMessageBox.Warning(self, u'Warning', u'请检测相机是否连接正确',
                                                        buttons=QtWidgets.QMessageBox.Ok,
                                                        defaultButton=QtWidgets.QMessageBox.Ok)
                else:
                    self.timer_cam.start(30)
                    self.btn_initcam.setText("Shutdown")
            else:
                self.timer_cam.stop()
                self.cap.release()
                self.lbl_displayImage.clear()
                self.btn_initcam.setText('InitCam')
        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./Resource/cig-logo.jpg"))
    myWin = RunWindow()
    myWin.show()
    sys.exit(app.exec_())