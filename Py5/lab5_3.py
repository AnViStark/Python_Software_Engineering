list = [1, 2, 3, 4, 5]
tmp = list[0]
list[0] = list[4]
list[4] = tmp
print(list)