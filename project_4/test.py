# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/roman/PycharmProjects/pythonProject/project_4/test.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(441, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.oldNum = QtWidgets.QLineEdit(self.centralwidget)
        self.oldNum.setGeometry(QtCore.QRect(10, 120, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.oldNum.setFont(font)
        self.oldNum.setObjectName("oldNum")
        self.oldType = QtWidgets.QLineEdit(self.centralwidget)
        self.oldType.setGeometry(QtCore.QRect(10, 210, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.oldType.setFont(font)
        self.oldType.setObjectName("oldType")
        self.newType = QtWidgets.QLineEdit(self.centralwidget)
        self.newType.setGeometry(QtCore.QRect(10, 310, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.newType.setFont(font)
        self.newType.setObjectName("newType")
        self.newNum = QtWidgets.QLineEdit(self.centralwidget)
        self.newNum.setGeometry(QtCore.QRect(10, 410, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.newNum.setFont(font)
        self.newNum.setObjectName("newNum")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.convert = QtWidgets.QPushButton(self.centralwidget)
        self.convert.setGeometry(QtCore.QRect(70, 490, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.convert.setFont(font)
        self.convert.setMouseTracking(False)
        self.convert.setAutoFillBackground(False)
        self.convert.setObjectName("convert")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.oldNum.setPlaceholderText(_translate("MainWindow", "Ваше число"))
        self.oldType.setPlaceholderText(_translate("MainWindow", "З якої системи (2, 8, 10,16)"))
        self.newType.setPlaceholderText(_translate("MainWindow", "В яку систему (2, 8, 10,16)"))
        self.newNum.setPlaceholderText(_translate("MainWindow", "Конвертоване число"))
        self.label.setText(_translate("MainWindow", "КОНВЕРТЕР ЧИСЕЛ"))
        self.convert.setText(_translate("MainWindow", "Конвертувати"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
