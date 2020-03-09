# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuopen = QtWidgets.QMenu(self.menubar)
        self.menuopen.setObjectName("menuopen")
        self.menuConfig = QtWidgets.QMenu(self.menubar)
        self.menuConfig.setObjectName("menuConfig")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionFile = QtWidgets.QAction(MainWindow)
        self.actionFile.setObjectName("actionFile")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionaa = QtWidgets.QAction(MainWindow)
        self.actionaa.setObjectName("actionaa")
        self.actionbb = QtWidgets.QAction(MainWindow)
        self.actionbb.setObjectName("actionbb")
        self.actioncc = QtWidgets.QAction(MainWindow)
        self.actioncc.setObjectName("actioncc")
        self.menuopen.addAction(self.actionFile)
        self.menuopen.addAction(self.actionExit)
        self.menuConfig.addAction(self.actionaa)
        self.menuConfig.addAction(self.actionbb)
        self.menuConfig.addAction(self.actioncc)
        self.menubar.addAction(self.menuopen.menuAction())
        self.menubar.addAction(self.menuConfig.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuopen.setTitle(_translate("MainWindow", "open"))
        self.menuConfig.setTitle(_translate("MainWindow", "Config"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionFile.setText(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionaa.setText(_translate("MainWindow", "aa"))
        self.actionbb.setText(_translate("MainWindow", "bb"))
        self.actioncc.setText(_translate("MainWindow", "cc"))
