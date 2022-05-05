import dataBaseVinjern
from design_2 import *
from PyQt5.QtWidgets import QMessageBox
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setWindowTitle("Шифрування-Дешифрування")
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
cript = True
cesar = ""

def chooseCesar():
    global cesar
    cesar = True
    ui.lineEdit_2.setPlaceholderText("Введіть ключ(1-32)")

def chooseVinjern():
    global cesar
    cesar = False
    ui.lineEdit_2.setPlaceholderText("Введіть ключ-cлово")

def criptScript():
    global cript
    ui.doResult.setText("Зашифрувати")
    ui.type.setText("Методи шифрування")
    cript = True

def decriptScript():
    global cript
    ui.doResult.setText("Розшифрувати")
    ui.type.setText("Методи дешифрування")
    cript = False

def doResult():
    global cript,cesar
    try:
        alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
        word = ui.word.text().lower()
        key = ui.lineEdit_2.text().lower()
        if all(list(map(lambda x:x in alphabet, list(word)))) and word != "":
            if cript:
                if cesar in [True,False]:
                    if cesar:
                        if key.isdigit():
                            cripted_alphabet = ""
                            for i in range(len(alphabet)):
                                if len(alphabet) - i <= int(key):
                                    cripted_alphabet += alphabet[-1 * (len(alphabet) - i) + int(key)]
                                else:
                                    cripted_alphabet += alphabet[i + int(key)]
                            ui.result.setText(word.translate(word.maketrans(alphabet,cripted_alphabet)))
                        else:
                            msg = QMessageBox()
                            msg.setWindowTitle("Повідомлення")
                            msg.setText("Введіть ключ числом(1-32)\t")
                            msg.exec_()
                    elif len(key) == len(word):
                        cripted = ""
                        for i in range(len(word)):
                            for x in dataBaseVinjern.baseVinjer:
                                if x[0] == word[i]:
                                    cripted += dataBaseVinjern.baseVinjer[0][x.index(key[i])]
                                    break
                        ui.result.setText(cripted)
                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Повідомлення")
                        msg.setText("Введіть ключ за довжиною такий ж самий як слово")
                        msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Повідомлення")
                    msg.setText("Виберіть метод шифрування\t")
                    msg.exec_()
            else:
                if cesar in [True, False]:
                    if cesar:
                        if key.isdigit():
                            decripted_alphabet = ""
                            for i in range(len(alphabet)):
                                if len(alphabet) - i <= int(key):
                                    decripted_alphabet += alphabet[-1 * (len(alphabet) - i) + int(key)]
                                else:
                                    decripted_alphabet += alphabet[i + int(key)]
                            ui.result.setText(word.translate(word.maketrans(decripted_alphabet, alphabet)))
                        else:
                            msg = QMessageBox()
                            msg.setWindowTitle("Повідомлення")
                            msg.setText("Введіть ключ за числом(1-32)\t")
                            msg.exec_()
                    elif len(key) == len(word):
                        decripted = ""
                        for i in range(len(word)):
                            index = dataBaseVinjern.baseVinjer[0].index(word[i])
                            for x in dataBaseVinjern.baseVinjer:
                                if x[index] == key[i]:
                                    decripted += x[0]
                                    break
                        ui.result.setText(decripted)
                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Повідомлення")
                        msg.setText("Введіть ключ за довжиною такий ж самий як слово")
                        msg.exec_()

                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Повідомлення")
                    msg.setText("Виберіть метод шифрування\t")
                    msg.exec_()

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Повідомлення")
            msg.setText("Введіть коректне слово\t")
            msg.exec_()
    except:
        pass
ui.cesar.toggled.connect(chooseCesar)
ui.vinjern.toggled.connect(chooseVinjern)
ui.cript.clicked.connect(criptScript)
ui.decript.clicked.connect(decriptScript)
ui.doResult.clicked.connect(doResult)
ui.cript.click()

sys.exit(app.exec_())