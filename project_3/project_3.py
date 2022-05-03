import random
from test import *
import sys
from PyQt5.QtWidgets import QMessageBox

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
size = 0
alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
field = []
cord = [0,0]
off_game =True

def generateField():
    global off_game,field,size,cord
    try:
        if off_game:
            size = int(ui.size.text())
            if size > 1:
                field = [[alphabet[random.randint(0, len(alphabet) - 1)] for i in range(size)] for i in range(size)]
                field[cord[0]][cord[1]] = "!"
                text = ""
                for i in range(size):
                    text += "    ".join(field[i]) + "\n"
                font = QtGui.QFont()
                font.setPointSize(int(300 / (size * 2.5)))
                ui.field.setFont(font)
                ui.field.setText(text[:-1])
                cord = [0, 0]
                off_game = False
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Повідомлення")
            msg.setText("Щоб почати нову гру вам потрібно завершити цю")
            msg.exec_()
    except:
        pass

def move():
    global cord,size,field,off_game
    try:
        letter = ui.letter.text()
        nearCord = [[cord[0], cord[1] + 1], [cord[0], cord[1] - 1], [cord[0] + 1, cord[1] + 1],[cord[0] - 1, cord[1] + 1], [cord[0] - 1, cord[1] - 1], [cord[0] + 1, cord[1] - 1],[cord[0] + 1, cord[1]], [cord[0] - 1, cord[1]]]
        for i in range(8):
            try:
                if field[nearCord[i][0]][nearCord[i][1]] == letter:
                    field[nearCord[i][0]][nearCord[i][1]], field[cord[0]][cord[1]] = field[cord[0]][cord[1]],field[nearCord[i][0]][nearCord[i][1]]
                    cord = nearCord[i]
                    ui.letter.clear()
                    break
            except:
                pass
        text = ""
        for i in range(size):
            text += "    ".join(field[i]) + "\n"
        ui.field.setText(text[:-1])
        if cord == [size - 1, size - 1]:
            msg = QMessageBox()
            msg.setWindowTitle("Congratulations")
            msg.setText("Мої вітання ви пройшли тепер ви можете почати заново")
            msg.exec_()
            cord = [0, 0]
            ui.field.clear()
            off_game = True
    except:
        pass
ui.generateField.clicked.connect(generateField)
ui.move.clicked.connect(move)

sys.exit(app.exec_())
