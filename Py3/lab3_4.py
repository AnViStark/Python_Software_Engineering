array = [123, 423, 212, 42, 2, 23, 77, 1334]
value = int(input("Значение для поиска: "))
if value in array:
    if value % 2 == 0:
        print("Переменная четная и есть в массиве")
    else:
        print("Переменная нечетная и есть в массиве")
else:
    print(f"Переменной нет в массиве и она равна {value}")