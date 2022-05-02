import sys
from test import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def convert():
    oldNum = ui.oldNum.text()
    oldType = int(ui.oldType.text())
    newType = int(ui.newType.text())
    if newType == 2:
        ui.newNum.setText(str(bin(int(oldNum, oldType))))
    elif newType == 8:
        ui.newNum.setText(str(oct(int(oldNum, oldType))))
    elif newType == 10:
        ui.newNum.setText(str(int(oldNum, oldType)))
    elif newType == 16:
        ui.newNum.setText(str(hex(int(oldNum, oldType))))
ui.convert.clicked.connect(convert)

sys.exit(app.exec_())