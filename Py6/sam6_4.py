def employee(tpl, number):
    new_tuple = list(tpl)
    if number in new_tuple:
        if new_tuple.count(number) == 1:
            new_tuple.index(number)
            new_tuple = tuple(new_tuple[new_tuple.index(number):])
            return new_tuple
        else:
            for i in range(new_tuple.index(number) + 1, len(new_tuple)):
                if new_tuple[i] == number:
                    new_tuple = tuple(new_tuple[new_tuple.index(number):i + 1])
                    break
            return new_tuple
    else:
        new_tuple = ()
        return new_tuple

print(employee((1, 2, 3), 8))
print(employee((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(employee((1, 2, 8, 5, 1, 2, 9), 8))