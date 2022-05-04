import random
from design_3 import *
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
off_game = True
moves = 0

def generateField():
    global off_game,field,size,cord, moves
    try:
        if off_game and ui.moves.value()>int(ui.size.text()):
            moves = ui.moves.value()
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
            msg.setText("Щоб почати гру вам потрібно вибрати приємлиму кількість ходів(Більшу за розмір поля)")
            msg.exec_()
            ui.moves.setValue(int(ui.size.text())+1)
    except:
        pass

def move():
    global cord,size,field,off_game,moves
    try:
        if field == []:
            msg = QMessageBox()
            msg.setWindowTitle("Повідомлення")
            msg.setText("  Зпочатку згенеруйте поле\t")
            msg.exec_()
        else:
            letter = ui.letter.text()
            ui.letter.clear()
            if not(letter in "qwertyuiopasdfghjklzxcvbnm,./;'[]1234567890-=/*+?><:!") and len(letter) == 1:
                moves -= 1
            nearCord = [[cord[0], cord[1] + 1], [cord[0], cord[1] - 1], [cord[0] + 1, cord[1] + 1],[cord[0] - 1, cord[1] + 1], [cord[0] - 1, cord[1] - 1], [cord[0] + 1, cord[1] - 1],[cord[0] + 1, cord[1]], [cord[0] - 1, cord[1]]]
            for i in range(8):
                try:
                    if field[nearCord[i][0]][nearCord[i][1]] == letter and nearCord[i][0] >= 0 and nearCord[i][1] >= 0:
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
                msg.setText("Мої вітання ви пройшли тепер ви можете почати заново!!!")
                msg.exec_()
                cord = [0, 0]
                ui.moves.setValue(0)
                ui.field.clear()
                ui.letter.clear()
                off_game = True
            elif moves == 0:
                msg = QMessageBox()
                msg.setWindowTitle("Ви програли")
                msg.setText("Ваші ходи вичерпані спробуйте заново заново")
                msg.exec_()
                cord = [0, 0]
                ui.field.clear()
                ui.letter.clear()
                off_game = True
    except:
        pass
ui.moves.setRange(0,100)
ui.generateField.clicked.connect(generateField)
ui.move.clicked.connect(move)

sys.exit(app.exec_())
