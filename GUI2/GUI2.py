# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI2'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1120, 864)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1111, 861))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 931, 831))
        self.graphicsView.setObjectName("graphicsView")
        self.btn_up = QtWidgets.QPushButton(self.tab)
        self.btn_up.setGeometry(QtCore.QRect(970, 110, 93, 28))
        self.btn_up.setObjectName("btn_up")
        self.btn_down = QtWidgets.QPushButton(self.tab)
        self.btn_down.setGeometry(QtCore.QRect(970, 180, 93, 28))
        self.btn_down.setObjectName("btn_down")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_up.setText(_translate("Dialog", "Up"))
        self.btn_down.setText(_translate("Dialog", "Down"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2"))
