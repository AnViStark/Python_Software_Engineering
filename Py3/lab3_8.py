value = 0
while value < 50:
    if value % 2 == 0:
        value += 7
    elif value % 5 == 0:
        value += 10
    else:
        value += 3
    print(value)