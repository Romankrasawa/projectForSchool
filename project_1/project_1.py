import random
from design_1 import *
from wordsBase import data_base
from PyQt5.QtWidgets import QMessageBox
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setWindowTitle("Поле чудес")
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
ui.widget.hide()
used = []
words = []
attempt = 0
"""

    """
def startGame():
    global words,attempt,used
    used = []
    ui.widget.show()
    ui.startMenu.hide()
    index = random.randint(0, len(data_base.keys()) - 1)
    words = ["".join(["_ " for i in list(data_base.values())[index]]), " ".join(list(data_base.values())[index])]
    ui.pidkazka.setText(str(list(data_base.keys())[index]).capitalize())
    attempt = len(list(set(list(words[1])))) + 2
    ui.lineEdit.setText(str(attempt))
    ui.word.setText(words[0])

def checkWord():
    global words,used,attempt
    letter = ui.letter.text().lower()
    if not(letter in "qwertyuiopasdfghjklzxcvbnm,./;'[]1234567890-=/*+?><:!") and len(letter) == 1 and not (letter in used):
        for i in range(len(words[1])):
            if words[1][i] == letter:
                words[0] = words[0][:i] + letter + words[0][i + 1:]
        ui.word.setText(words[0].capitalize())
        ui.letter.clear()
        used.append(letter)
        attempt-=1
        ui.lineEdit.setText(str(attempt))
    elif (letter in used):
        msg = QMessageBox()
        msg.setWindowTitle("Повідомлення")
        msg.setText("Ви ввели використану букву, введіть іншу")
        msg.exec_()
        ui.letter.clear()
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Повідомлення")
        msg.setText("\tВи ввели некоректну букву\t")
        msg.exec_()
        ui.letter.clear()
    if not ("_" in words[0]):
        msg = QMessageBox()
        msg.setWindowTitle("Congratulations")
        msg.setText("\tМої вітання ви вгадали слово!!!\t")
        msg.exec_()
        ui.letter.clear()
        ui.widget.hide()
        ui.startMenu.show()
    elif attempt == 0:
        msg = QMessageBox()
        msg.setWindowTitle("Повідомлення")
        msg.setText("Ваші спроби вичерпались спробуйте ще раз!!!")
        msg.exec_()
        ui.letter.clear()
        ui.widget.hide()
        ui.startMenu.show()
ui.startButton.clicked.connect(startGame)
ui.pushButton_2.clicked.connect(checkWord)
sys.exit(app.exec_())