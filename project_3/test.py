# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/roman/PycharmProjects/pythonProject/project_3/test.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(447, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.field = QtWidgets.QTextEdit(self.centralwidget)
        self.field.setGeometry(QtCore.QRect(60, 180, 321, 271))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Telugu")
        font.setBold(True)
        font.setWeight(75)
        self.field.setFont(font)
        self.field.setReadOnly(True)
        self.field.setObjectName("field")
        self.size = QtWidgets.QLineEdit(self.centralwidget)
        self.size.setGeometry(QtCore.QRect(10, 120, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.size.setFont(font)
        self.size.setObjectName("size")
        self.generateField = QtWidgets.QPushButton(self.centralwidget)
        self.generateField.setGeometry(QtCore.QRect(240, 110, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.generateField.setFont(font)
        self.generateField.setObjectName("generateField")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 0, 371, 121))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.letter = QtWidgets.QLineEdit(self.centralwidget)
        self.letter.setGeometry(QtCore.QRect(70, 460, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.letter.setFont(font)
        self.letter.setObjectName("letter")
        self.move = QtWidgets.QPushButton(self.centralwidget)
        self.move.setGeometry(QtCore.QRect(230, 520, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.move.setFont(font)
        self.move.setObjectName("move")
        self.moves = QtWidgets.QSpinBox(self.centralwidget)
        self.moves.setGeometry(QtCore.QRect(140, 530, 61, 41))
        self.moves.setObjectName("moves")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 520, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.size.setPlaceholderText(_translate("MainWindow", "Введіть розмір для поля"))
        self.generateField.setText(_translate("MainWindow", "Згенерувати"))
        self.label.setText(_translate("MainWindow", "ГРА З БУКВАМИ"))
        self.letter.setPlaceholderText(_translate("MainWindow", "Введіть букву для переміщення"))
        self.move.setText(_translate("MainWindow", "Переміститися"))
        self.label_2.setText(_translate("MainWindow", "Кількість ходів"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
