# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cigauto.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1033, 719)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 120, 641, 101))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_goback = QtWidgets.QPushButton(self.centralwidget)
        self.btn_goback.setGeometry(QtCore.QRect(280, 320, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_goback.setFont(font)
        self.btn_goback.setObjectName("btn_goback")
        self.display_User = QtWidgets.QLabel(self.centralwidget)
        self.display_User.setGeometry(QtCore.QRect(920, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.display_User.setFont(font)
        self.display_User.setText("")
        self.display_User.setObjectName("display_User")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(520, 60, 191, 31))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(590, 320, 222, 48))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(740, 60, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(740, 100, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.txt_display_datetime = QtWidgets.QLabel(self.centralwidget)
        self.txt_display_datetime.setGeometry(QtCore.QRect(630, 10, 191, 21))
        self.txt_display_datetime.setText("")
        self.txt_display_datetime.setObjectName("txt_display_datetime")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(830, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn_enter = QtWidgets.QPushButton(self.centralwidget)
        self.btn_enter.setGeometry(QtCore.QRect(340, 470, 93, 28))
        self.btn_enter.setObjectName("btn_enter")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1033, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())



        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_enter.clicked.connect(self.btnClicked)

    def btnClicked(self):
        #QMessageBox.information(self, "Result", str(m+n))
        QMessageBox.information(self, "Result", "Test!!!")

    def actionEnter(self):
        # QMessageBox.information(self,"Welcome to cigauto ...")
        #print("aaaa")
        #QtWidgets.QMessageBox.information(self, "aaaaaa....")
        QMessageBox.information(self, "消息框标题", "这是一条消息。", QMessageBox.Yes | QMessageBox.No)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "恭喜您，您已成功登陆！！！"))
        self.btn_goback.setText(_translate("MainWindow", "返回登陆界面"))
        self.commandLinkButton.setText(_translate("MainWindow", "进入"))
        self.label_2.setText(_translate("MainWindow", "Login User:"))
        self.btn_enter.setText(_translate("MainWindow", "Enter"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
