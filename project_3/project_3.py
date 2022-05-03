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
moves = 0

def generateField():
    global off_game,field,size,cord, moves
    try:
        moves = ui.moves.value()
        if off_game and moves>0:
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
        elif not(off_game):
            msg = QMessageBox()
            msg.setWindowTitle("Повідомлення")
            msg.setText("Щоб почати нову гру вам потрібно завершити цю")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Повідомлення")
            msg.setText("Щоб почати гру вам потрібно вибрати приємлиму кількість ходів")
            msg.exec_()
    except:
        pass

def move():
    global cord,size,field,off_game,moves
    try:
        if moves == 0:
            msg = QMessageBox()
            msg.setWindowTitle("Ви програли")
            msg.setText("Ваші ходи вичерпані спробуйте заново заново")
            msg.exec_()
            cord = [0, 0]
            ui.field.clear()
            ui.letter.clear()
            off_game = True
        else:
            letter = ui.letter.text()
            ui.letter.clear()
            if not(letter in "qwertyuiopasdfghjklzxcvbnm,./;'[]1234567890-=/*+?><:!") and len(letter) == 1:
                moves -= 1
            nearCord = [[cord[0], cord[1] + 1], [cord[0], cord[1] - 1], [cord[0] + 1, cord[1] + 1],[cord[0] - 1, cord[1] + 1], [cord[0] - 1, cord[1] - 1], [cord[0] + 1, cord[1] - 1],[cord[0] + 1, cord[1]], [cord[0] - 1, cord[1]]]
            for i in range(8):
                try:
                    if field[nearCord[i][0]][nearCord[i][1]] == letter:
                        field[nearCord[i][0]][nearCord[i][1]], field[cord[0]][cord[1]] = field[cord[0]][cord[1]],field[nearCord[i][0]][nearCord[i][1]]
                        cord = nearCord[i]
                        break
                except:
                    pass
            text = ""
            for i in range(size):
                text += "    ".join(field[i]) + "\n"
            ui.field.setText(text[:-1])
            ui.moves.setValue(moves)
            if cord == [size - 1, size - 1]:
                msg = QMessageBox()
                msg.setWindowTitle("Congratulations")
                msg.setText("Мої вітання ви пройшли тепер ви можете почати заново")
                msg.exec_()
                cord = [0, 0]
                ui.moves.setValue(0)
                ui.field.clear()
                ui.letter.clear()
                off_game = True
    except:
        pass
ui.generateField.clicked.connect(generateField)
ui.move.clicked.connect(move)

sys.exit(app.exec_())
