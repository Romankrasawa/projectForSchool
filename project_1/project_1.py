import random

data_base = {"Принтер навпаки":"сканер","Підлога навпаки":"стеля","Сонце навпаки":"місяць"}
index = random.randint(0,len(data_base.keys())-1)
used = []
print(list(data_base.keys())[index])
words = ["".join(["_ " for i in list(data_base.values())[index]])," ".join(list(data_base.values())[index])]
print(words)
print(words[0])
while True:
    letter = input("Введіть букву: ")
    if not(letter in used):
        for i in range(len(words[1])):
            if words[1][i] == letter:
                words[0] = words[0][:i]+letter+words[0][i+1:]
        print(words[0].capitalize())
        used.append(letter)
    else:
        print("Ви ввели використану букву")
    if not("_" in words[0]):
        break