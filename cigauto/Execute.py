from PyQt5 import QtWidgets
import Login
import cigauto
import cigauto2
import time
import os
import datetime
from PyQt5.QtCore import QTime, QDateTime, QTimer
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
os.environ["CUDA_VISIBLE_DEVICES"] = "2"

def user_login(self):

    msg = None
    user = ui.txt_username.text()
    pwd = ui.txt_passwd.text()
    opt = ui.cmb_optor.currentText()

    if opt == "管理员":
        if user == 'admin':
            if pwd == 'admin':
                login_win.close()

                main_ui.display_User.setText(user)
                main_window.show()
            else:
                #print(pwd,"---", user)
                msg = "Fail: password is invalid !!!"
        else:
            msg = "Fail: No this admin user !!!"

        ui.lbl_msg.setText(msg)

    else:
        if user == 'cig':
            if pwd == '123':
                Login.close()
                cigauto.show()
            else:
                msg = "Failed: password is invalid !!!"
        else:
            msg = "Failed: No this user !!!"

        ui.lbl_msg.setText(msg)


def go_back(self):
    main_window.close()
    login_win.show()



def display_user(self):
    user = ui.txt_username.text()
    main_ui.display_User.setText(user)

def showtime(self):
    datetime = QDateTime.currentDateTime()
    text = datetime.toString()
    main_ui.txt_display_datetime.setText("     " + text)

def set_background_image(self):
    #palette = QtGui.QPalette()
    image = QtGui.QPixmap("./Resource/login.jpg")
    image = image.scaled(1033, 719)
    #main_ui.palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(image))
    #main_ui.setPalette(main_ui.palette)

def move_window_center(self):
    screen = QDesktopWidget().screenGeometry()
    size = self.geometry()
    new_left = (screen.width()- size.width())/2
    new_top = (screen.height() - size.height())/2
    self.move(new_left,new_top)

def actionEnter(self):

    #QMessageBox.information(self,"Welcome to cigauto ...")
    print("aaaa")
    QMessageBox.information(self, "aaaaaa....")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setWindowIcon(QIcon("./Resource/cig-logo.jpg"))
    login_win = QtWidgets.QWidget()
    ui = Login.Ui_Form()
    ui.setupUi(login_win)  # 启动运行
    #move_window_center(ui)
    ui.btn_login.clicked.connect(user_login)  # 设置登陆界面按钮点击事件
    #ui.btn_cancel.clicked.connect(QtWidgets.QWidget.close)
    main_window = QtWidgets.QMainWindow()
    main_ui = cigauto.Ui_MainWindow()
    main_ui.setupUi(main_window)  # 启动运行

    #set_background_image(main_ui)

    main_ui.btn_goback.clicked.connect(go_back)  # 设置调试界面按钮点击事件
    #main_ui.btn_enter.clicked.connect(actionEnter)
    login_win.show()
