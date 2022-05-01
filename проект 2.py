import dataBaseVinjern

alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
encript = int(input("Шифрувати(1) чи розшифровувати(0):"))
if encript == 1:
    cripting = int(input("Спосіб кодування (1(шифр цезаря) або 0(шифр вінжерна)):"))
    word = input("Введіть слово для шифрування: ")
    def cesar(key):
        cripted_alphabet = ""
        for i in range(len(alphabet)):
            if len(alphabet) - i <= key:
                cripted_alphabet += alphabet[-1 * (len(alphabet) - i) + key]
            else:
                cripted_alphabet += alphabet[i + key]
        return word.translate(word.maketrans(alphabet,cripted_alphabet))

    def vinjern(key):
        cripted = ""
        for i in range(len(word)):
            for x in dataBaseVinjern.baseVinjer:
                if x[0] == word[i]:
                    cripted += dataBaseVinjern.baseVinjer[0][x.index(key[i])]
                    break
        return cripted
    if cripting == 1:
        print(cesar(int(input("Введіть ключ: "))))

    else:
        print(vinjern(input("Введіть ключ: ")))
else:
    decripting = int(input("Спосіб декодування (1(шифр цезаря) або 0(шифр вінжерна)):"))
    word = input("Введіть слово для розшифрування: ")

    def decriptCesar(key):
        decripted_alphabet = ""
        for i in range(len(alphabet)):
            if len(alphabet) - i <= key:
                decripted_alphabet += alphabet[-1 * (len(alphabet) - i) + key]
            else:
                decripted_alphabet += alphabet[i + key]
        return word.translate(word.maketrans(decripted_alphabet, alphabet))

    def decriptVinjern(key):
        decripted = ""
        for i in range(len(word)):
            index = dataBaseVinjern.baseVinjer[0].index(word[i])
            for x in dataBaseVinjern.baseVinjer:
                if x[index] == key[i]:
                    decripted += x[0]
                    break
        return decripted

    if decripting == 1:
        print(decriptCesar(int(input("Введіть ключ: "))))

    else:
        print(decriptVinjern(input("Введіть ключ: ")))