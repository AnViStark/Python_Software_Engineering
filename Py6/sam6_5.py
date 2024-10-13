def finder(t):
    max_inc = [t[0]]
    max_dec = [t[0]]
    tmp_inc = [t[0]]
    tmp_dec = [t[0]]
    
    for i in range(1, len(t)):
        if t[i] > t[i - 1]:
            tmp_inc.append(t[i])
            if len(tmp_inc) > len(max_inc):
                max_inc = tmp_inc[:]
            tmp_dec = [t[i]]
        elif t[i] < t[i - 1]:
            tmp_dec.append(t[i])
            if len(tmp_dec) > len(max_dec):
                max_dec = tmp_dec[:]
            tmp_inc = [t[i]]

    if not max_inc:
        max_inc = [t[0]]
    if not max_dec:
        max_dec = [t[0]]

    return tuple(max_inc), tuple(max_dec)

print(finder((1, 2, 3, 2, 1, 4, 5, 1, 2)))
print(finder((5, 4, 3, 2, 1)))
print(finder((1, 3, 5, 7, 9)))

#Создайте программу, которая получает на вход кортеж из последовательности чисел. Программа должна находить максимальную и минимальную длину последовательных возрастающих и убывающих подпоследовательностей в исходном кортеже. Необходимо вернуть два кортежа: один с максимальной длиной возрастающей подпоследовательности, а второй — с максимальной длиной убывающей подпоследовательности.