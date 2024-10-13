data = input("Введите числа через пробел: ")

list = data.split()
list = [int(x) for x in list]
print(list)

my_tuple = tuple(list)
print(my_tuple)