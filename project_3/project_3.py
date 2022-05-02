import random

alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
size = int(input("Введіть розмір поля: "))
field = [[alphabet[random.randint(0,len(alphabet)-1)] for i in range(size)] for i in range(size)]
cord = [0,0]
field[cord[0]][cord[1]] = "!"
while cord != [size-1,size-1]:
    for i in range(size):
        print(field[i])
    letter = input("\nВведіть букву: ")
    nearCord = [[cord[0],cord[1]+1],[cord[0],cord[1]-1],[cord[0]+1,cord[1]+1],[cord[0]-1,cord[1]+1],[cord[0]-1,cord[1]-1],[cord[0]+1,cord[1]-1],[cord[0]+1,cord[1]],[cord[0]-1,cord[1]]]
    for i in range(8):
        try:
            if field[nearCord[i][0]][nearCord[i][1]] == letter:
                field[nearCord[i][0]][nearCord[i][1]],field[cord[0]][cord[1]] = field[cord[0]][cord[1]],field[nearCord[i][0]][nearCord[i][1]]
                cord = nearCord[i]
                break
        except:
            pass
for i in range(size):
    print(field[i])
print("Ви виграли")
