# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menu(object):
    def setupUi(self, menu):
        menu.setObjectName("menu")
        menu.setFixedSize(341, 258)
        menu.setStyleSheet("font: 8pt \"Segoe Script\";")
        self.autr = QtWidgets.QPushButton(menu)
        self.autr.setEnabled(True)
        self.autr.setGeometry(QtCore.QRect(20, 20, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.autr.setFont(font)
        self.autr.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.227273 rgba(255, 203, 81, 237), stop:0.886364 rgba(255, 134, 73, 255));\n"
"border: 2px solid #ff7474;\n"
"border-radius: 10px;\n"
"font: 75 25pt \"Comic Sans MS\";")
        self.autr.setObjectName("autr")
        self.reg = QtWidgets.QPushButton(menu)
        self.reg.setEnabled(True)
        self.reg.setGeometry(QtCore.QRect(20, 80, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(21)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.reg.setFont(font)
        self.reg.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.227273 rgba(255, 203, 81, 237), stop:0.886364 rgba(255, 134, 73, 255));\n"
"border: 2px solid #ff7474;\n"
"border-radius: 10px;\n"
"font: 75 21pt \"Comic Sans MS\";")
        self.reg.setObjectName("reg")
        self.getpas = QtWidgets.QPushButton(menu)
        self.getpas.setEnabled(True)
        self.getpas.setGeometry(QtCore.QRect(10, 160, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.getpas.setFont(font)
        self.getpas.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.227273 rgba(255, 203, 81, 237), stop:0.886364 rgba(255, 134, 73, 255));\n"
"border: 2px solid #ff7474;\n"
"border-radius: 10px;\n"
"font: 75 16pt \"Comic Sans MS\";")
        self.getpas.setObjectName("getpas")
        self.back = QtWidgets.QPushButton(menu)
        self.back.setGeometry(QtCore.QRect(10, 210, 101, 31))
        self.back.setStyleSheet("background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.227273 rgba(255, 203, 81, 237), stop:0.886364 rgba(255, 134, 73, 255));\n"
"border: 2px solid #ff7474;\n"
"border-radius: 10px;\n"
"font: 75 12pt \"Comic Sans MS\";")
        self.back.setObjectName("back")
        self.widget = QtWidgets.QWidget(menu)
        self.widget.setGeometry(QtCore.QRect(-220, -200, 801, 551))
        self.widget.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0.227273 rgba(149, 255, 247, 237), stop:0.886364 rgba(201, 107, 255, 255));")
        self.widget.setObjectName("widget")
        self.widget.raise_()
        self.autr.raise_()
        self.reg.raise_()
        self.getpas.raise_()
        self.back.raise_()

        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)

    def retranslateUi(self, menu):
        _translate = QtCore.QCoreApplication.translate
        menu.setWindowTitle(_translate("menu", "Form"))
        self.autr.setText(_translate("menu", "??????????"))
        self.reg.setText(_translate("menu", "????????????????????????????????????"))
        self.getpas.setText(_translate("menu", "???????????????????????????? ????????????????"))
        self.back.setText(_translate("menu", "<-- ??????????"))
