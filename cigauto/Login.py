# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QBrush, QPixmap

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(584, 515)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 213, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 213, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 213, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 213, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(94, 35, 411, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(200, 138, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #palette.setBrush(QPalette.Background, QBrush(QPixmap("./Resource/login.jpg")))
        #Form.setPalette(palette)
        #Form.resize(584, 515)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 138, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setUnderline(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 160, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.cmb_optor = QtWidgets.QComboBox(Form)
        self.cmb_optor.setGeometry(QtCore.QRect(230, 160, 171, 31))
        self.cmb_optor.setObjectName("cmb_optor")
        self.cmb_optor.addItem("")
        self.cmb_optor.addItem("")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(150, 280, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(130, 220, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txt_username = QtWidgets.QLineEdit(Form)
        self.txt_username.setGeometry(QtCore.QRect(230, 220, 171, 31))
        self.txt_username.setObjectName("txt_username")
        self.txt_passwd = QtWidgets.QLineEdit(Form)
        self.txt_passwd.setGeometry(QtCore.QRect(230, 280, 171, 31))
        self.txt_passwd.setObjectName("txt_passwd")
        self.btn_login = QtWidgets.QPushButton(Form)
        self.btn_login.setGeometry(QtCore.QRect(130, 360, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
        self.btn_cancel = QtWidgets.QPushButton(Form)
        self.btn_cancel.setGeometry(QtCore.QRect(320, 360, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setObjectName("btn_cancel")
        self.lbl_msg = QtWidgets.QLabel(Form)
        self.lbl_msg.setGeometry(QtCore.QRect(130, 440, 401, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lbl_msg.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_msg.setFont(font)
        self.lbl_msg.setText("")
        self.lbl_msg.setObjectName("lbl_msg")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        self.label.setText(_translate("Form", "Welcom CIG Automation"))
        self.label_2.setText(_translate("Form", "操作权限："))
        self.cmb_optor.setItemText(0, _translate("Form", "管理员"))
        self.cmb_optor.setItemText(1, _translate("Form", "操作员"))
        self.label_3.setText(_translate("Form", "密码："))
        self.label_4.setText(_translate("Form", "用户名："))
        self.btn_login.setText(_translate("Form", "Login"))
        self.btn_cancel.setText(_translate("Form", "Cancel"))
import Resource_rc