# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 640)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 560, 431, 71))
        self.textEdit.setObjectName("textEdit")

        self.nameInput = QtWidgets.QTextEdit(self.centralwidget)
        self.nameInput.setGeometry(QtCore.QRect(10, 10, 150, 31))
        self.nameInput.setObjectName("nameInput")

        self.scrollAreaUser = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaUser.setGeometry(QtCore.QRect(10, 50, 100, 500))
        self.scrollAreaUser.setWidgetResizable(True)
        self.scrollAreaUser.setObjectName("scrollAreaUser")
        self.users = QtWidgets.QWidget()
        self.users.setMinimumSize(50, 2000)
        self.scrollAreaUser.setWidget(self.users)


        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(119, 50, 380, 500))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.history = QtWidgets.QWidget()
        self.history.setMinimumSize(150, 2000)
        self.scrollArea.setWidget(self.history)
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setText("发送")
        self.submit.move(440, 603)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
