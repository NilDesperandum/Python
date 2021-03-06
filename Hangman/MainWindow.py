# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 339)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelWord = QtWidgets.QLabel(self.centralwidget)
        self.labelWord.setObjectName("labelWord")
        self.verticalLayout.addWidget(self.labelWord)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelProby = QtWidgets.QLabel(self.centralwidget)
        self.labelProby.setMinimumSize(QtCore.QSize(200, 0))
        self.labelProby.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.labelProby.setObjectName("labelProby")
        self.horizontalLayout_2.addWidget(self.labelProby, 0, QtCore.Qt.AlignHCenter)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setMinimumSize(QtCore.QSize(100, 0))
        self.lcdNumber.setMaximumSize(QtCore.QSize(100, 50))
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setProperty("intValue", 10)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_2.addWidget(self.lcdNumber, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(100, 50))
        self.lineEdit.setMaximumSize(QtCore.QSize(100, 50))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.zgadujButton = QtWidgets.QPushButton(self.centralwidget)
        self.zgadujButton.setObjectName("zgadujButton")
        self.horizontalLayout.addWidget(self.zgadujButton)
        self.wyjdzButton = QtWidgets.QPushButton(self.centralwidget)
        self.wyjdzButton.setObjectName("wyjdzButton")
        self.horizontalLayout.addWidget(self.wyjdzButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 638, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hangman"))
        self.labelWord.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">**********</p></body></html>"))
        self.labelProby.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Pozostałe próby:</p></body></html>"))
        self.zgadujButton.setText(_translate("MainWindow", "Zgaduj"))
        self.wyjdzButton.setText(_translate("MainWindow", "Wyjdź"))
