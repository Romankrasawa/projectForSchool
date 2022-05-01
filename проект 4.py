a = input("Введіть число\t")
old = int(input("Старий тип\t"))
new = int(input("Новий тип\t"))
if new  == 2:
    print("Нове число = ",bin(int(a,old)))
elif new == 8:
    print("Нове число = ",oct(int(a, old)))
elif new == 10:
    print("Нове число = ",int(a, old))
elif new == 16:
    print("Нове число = ",hex(int(a, old)))