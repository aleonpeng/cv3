# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WinGet'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import winget_rc

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1113, 860)
        #Form.setStyleSheet("QWidGet{Border-image:url(:/cig/CIG.jpg)}")
        Form.setStyleSheet("QWidGet{border-image:url(C:/Users/Allen/PycharmProjects/cv3/WinGet/cig/CIG.jpg);}")

        self.btn_Ok = QtWidgets.QPushButton(Form)
        self.btn_Ok.setGeometry(QtCore.QRect(920, 110, 93, 28))
        self.btn_Ok.setObjectName("btn_Ok")
        self.btn_Cancel = QtWidgets.QPushButton(Form)
        self.btn_Cancel.setGeometry(QtCore.QRect(920, 200, 93, 28))
        self.btn_Cancel.setObjectName("btn_Cancel")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(40, 300, 491, 421))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 30, 141, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 30, 141, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(680, 490, 291, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Slider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Slider.setObjectName("Slider")
        self.verticalLayout.addWidget(self.Slider)
        self.lcd = QtWidgets.QLCDNumber(Form)
        self.lcd.setGeometry(QtCore.QRect(680, 340, 291, 141))
        self.lcd.setObjectName("lcd")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_Ok.setText(_translate("Form", "OK"))
        self.btn_Cancel.setText(_translate("Form", "Cancel"))
        self.graphicsView.setToolTip(_translate("Form", "<html><head/><body><p>Here is show image.</p></body></html>"))
        self.pushButton.setToolTip(_translate("Form", "<html><head/><body><p>This is down key.</p></body></html>"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.pushButton_2.setToolTip(_translate("Form", "<html><head/><body><p>This is Up key.</p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))

