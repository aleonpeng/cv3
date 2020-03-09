# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dWinForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1269, 865)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1041, 811))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_displayImage = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_displayImage.setObjectName("lbl_displayImage")
        self.horizontalLayout.addWidget(self.lbl_displayImage)
        self.btn_initcam = QtWidgets.QPushButton(self.centralwidget)
        self.btn_initcam.setGeometry(QtCore.QRect(1080, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_initcam.setFont(font)
        self.btn_initcam.setObjectName("btn_initcam")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1269, 26))
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
        self.actionui = QtWidgets.QAction(MainWindow)
        self.actionui.setObjectName("actionui")
        self.actionbb = QtWidgets.QAction(MainWindow)
        self.actionbb.setObjectName("actionbb")
        self.actionaa = QtWidgets.QAction(MainWindow)
        self.actionaa.setObjectName("actionaa")
        self.actionreference = QtWidgets.QAction(MainWindow)
        self.actionreference.setObjectName("actionreference")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menuSetting.addAction(self.actionui)
        self.menuSetting.addAction(self.actionbb)
        self.menuSetting.addAction(self.actionaa)
        self.menuHelp.addAction(self.actionreference)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_displayImage.setText(_translate("MainWindow", "TextLabel"))
        self.btn_initcam.setText(_translate("MainWindow", "InitialCam"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionui.setText(_translate("MainWindow", "ui"))
        self.actionbb.setText(_translate("MainWindow", "bb"))
        self.actionaa.setText(_translate("MainWindow", "aa"))
        self.actionreference.setText(_translate("MainWindow", "reference"))
