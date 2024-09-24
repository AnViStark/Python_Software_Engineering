string = "Строка, чтобы искать в ней буквы"
value = input("Введите букву, которую хотите найти: ")
for i in string:
    if i == value:
        print(f"Буква {value} есть в строке")
        break
else:
    print(f"Буквы {value} нет в строке")