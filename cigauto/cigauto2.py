# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cigauto2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1058, 841)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(260, 160, 581, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_goback = QtWidgets.QPushButton(Form)
        self.btn_goback.setGeometry(QtCore.QRect(310, 410, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_goback.setFont(font)
        self.btn_goback.setObjectName("btn_goback")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 420, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "欢迎来到PYQT的自动化世界！！！"))
        self.btn_goback.setText(_translate("Form", "返回登陆界面"))
        self.pushButton_2.setText(_translate("Form", "进入。。。。"))
