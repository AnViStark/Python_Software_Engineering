array = [2, 4, 5, 8, 12]
flag = False
for i in array:
    if i % 2 == 1:
        flag = True
if flag is True:
    print("В массиве есть нечетное число")
else:
    print("В массиве нет нечетных чисел")