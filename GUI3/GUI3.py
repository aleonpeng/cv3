# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI3'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

#import GUI3_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")

        Dialog.resize(1118, 861)
        self.ImageDir = QtWidgets.QGraphicsView(Dialog)
        self.ImageDir.setGeometry(QtCore.QRect(30, 110, 691, 571))
        self.ImageDir.setAutoFillBackground(True)
        brush = QtGui.QBrush(QtGui.QColor(0, 126, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.ImageDir.setBackgroundBrush(brush)
        self.ImageDir.setObjectName("ImageDir")
        self.btn_start = QtWidgets.QPushButton(Dialog)
        self.btn_start.setGeometry(QtCore.QRect(170, 10, 131, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_start.setFont(font)
        self.btn_start.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.btn_start.setObjectName("btn_start")
        self.btn_stop = QtWidgets.QPushButton(Dialog)
        self.btn_stop.setGeometry(QtCore.QRect(410, 10, 121, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_stop.setFont(font)
        self.btn_stop.setObjectName("btn_stop")
        self.timeEdit = QtWidgets.QTimeEdit(Dialog)
        self.timeEdit.setGeometry(QtCore.QRect(980, 40, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(740, 110, 361, 171))
        self.textEdit.setObjectName("textEdit")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(780, 330, 271, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(800, 400, 231, 191))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        #self.
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_start.setText(_translate("Dialog", "Start"))
        self.btn_stop.setText(_translate("Dialog", "Stop"))
        self.btn_start.setIcon(QtGui.QIcon(QtGui.QPixmap("Resource/play1hot.png")))
        #self.btn_start.
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hello world, Iam Allen</p></body></html>"))
        self.comboBox.setItemText(0, _translate("Dialog", "0"))
        self.comboBox.setItemText(1, _translate("Dialog", "1"))
        self.comboBox.setItemText(2, _translate("Dialog", "2"))
        self.comboBox.setItemText(3, _translate("Dialog", "3"))
        self.comboBox.setItemText(4, _translate("Dialog", "4"))
        self.comboBox.setItemText(5, _translate("Dialog", "5"))
        self.comboBox.setItemText(6, _translate("Dialog", "6"))
        self.comboBox.setItemText(7, _translate("Dialog", "7"))
        self.label.setText(_translate("Dialog", "TextLabel"))



