# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/roman/PycharmProjects/pythonProject/project_2/design_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 565)
        MainWindow.setStyleSheet("background-color:#E9D5DA;\n"
"font: 50 13pt \"Yu Gothic Medium\";\n"
"color:white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cript = QtWidgets.QPushButton(self.centralwidget)
        self.cript.setGeometry(QtCore.QRect(0, 10, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(6)
        self.cript.setFont(font)
        self.cript.setStyleSheet("background-color: rgb(130, 115, 151);")
        self.cript.setObjectName("cript")
        self.decript = QtWidgets.QPushButton(self.centralwidget)
        self.decript.setGeometry(QtCore.QRect(220, 10, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(6)
        self.decript.setFont(font)
        self.decript.setStyleSheet("background-color: rgb(130, 115, 151);")
        self.decript.setObjectName("decript")
        self.cesar = QtWidgets.QRadioButton(self.centralwidget)
        self.cesar.setGeometry(QtCore.QRect(0, 210, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(6)
        self.cesar.setFont(font)
        self.cesar.setObjectName("cesar")
        self.vinjern = QtWidgets.QRadioButton(self.centralwidget)
        self.vinjern.setGeometry(QtCore.QRect(0, 280, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(6)
        self.vinjern.setFont(font)
        self.vinjern.setObjectName("vinjern")
        self.type = QtWidgets.QLabel(self.centralwidget)
        self.type.setGeometry(QtCore.QRect(0, 130, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(6)
        self.type.setFont(font)
        self.type.setObjectName("type")
        self.word = QtWidgets.QLineEdit(self.centralwidget)
        self.word.setGeometry(QtCore.QRect(210, 190, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(6)
        self.word.setFont(font)
        self.word.setStyleSheet("")
        self.word.setObjectName("word")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 280, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(6)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.result = QtWidgets.QLineEdit(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(10, 390, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(6)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.labelWord = QtWidgets.QLabel(self.centralwidget)
        self.labelWord.setGeometry(QtCore.QRect(210, 150, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(6)
        self.labelWord.setFont(font)
        self.labelWord.setObjectName("labelWord")
        self.labelKey = QtWidgets.QLabel(self.centralwidget)
        self.labelKey.setGeometry(QtCore.QRect(210, 240, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(6)
        self.labelKey.setFont(font)
        self.labelKey.setObjectName("labelKey")
        self.doResult = QtWidgets.QPushButton(self.centralwidget)
        self.doResult.setGeometry(QtCore.QRect(100, 470, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(6)
        self.doResult.setFont(font)
        self.doResult.setStyleSheet("background-color: rgb(130, 115, 151);")
        self.doResult.setObjectName("doResult")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 350, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(6)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cript.setText(_translate("MainWindow", "????????????????????"))
        self.decript.setText(_translate("MainWindow", "????????????????????????"))
        self.cesar.setText(_translate("MainWindow", "???????? ????????????"))
        self.vinjern.setText(_translate("MainWindow", "???????? ????????????????"))
        self.type.setText(_translate("MainWindow", "TextLabel"))
        self.word.setPlaceholderText(_translate("MainWindow", "?????????????? ??????????"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "?????????????? ????????"))
        self.labelWord.setText(_translate("MainWindow", "??????????"))
        self.labelKey.setText(_translate("MainWindow", "???????? ????????????????????"))
        self.doResult.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "??????????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
