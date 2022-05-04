import sys
from design_4 import *
from PyQt5.QtWidgets import QMessageBox

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def convert():
    try:
        oldNum = ui.oldNum.text()
        oldType = ui.oldType.text()
        newType = ui.newType.text()
        if not(oldNum.isdigit()) or not(oldType.isdigit()) or not(newType).isdigit():
            msg = QMessageBox()
            msg.setWindowTitle("Помилка")
            msg.setText("  Ви ввелили некоректні дані\t")
            msg.exec_()
        elif newType == oldType:
            msg = QMessageBox()
            msg.setWindowTitle("Повідомлення")
            msg.setText("Системи даних співпадають введіть їх різними")
            msg.exec_()
        elif int(newType) == 2:
            ui.newNum.setText(str(bin(int(oldNum, int(oldType)))))
        elif int(newType) == 8:
            ui.newNum.setText(str(oct(int(oldNum, int(oldType)))))
        elif int(newType) == 10:
            ui.newNum.setText(str(int(oldNum, int(oldType))))
        elif int(newType) == 16:
            ui.newNum.setText(str(hex(int(oldNum, int(oldType)))))
    except:
        pass
ui.convert.clicked.connect(convert)

sys.exit(app.exec_())