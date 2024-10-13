def finder(tpl):
    max_inc = [tpl[0]]
    max_dec = [tpl[0]]
    tmp_inc = [tpl[0]]
    tmp_dec = [tpl[0]]
    
    for i in range(1, len(tpl)):
        if tpl[i] > tpl[i - 1]:
            tmp_inc.append(tpl[i])
            if len(tmp_inc) > len(max_inc):
                max_inc = tmp_inc[:]
            tmp_dec = [tpl[i]]
        elif tpl[i] < tpl[i - 1]:
            tmp_dec.append(tpl[i])
            if len(tmp_dec) > len(max_dec):
                max_dec = tmp_dec[:]
            tmp_inc = [tpl[i]]

    if not max_inc:
        max_inc = [tpl[0]]
    if not max_dec:
        max_dec = [tpl[0]]

    return tuple(max_inc), tuple(max_dec)

print(finder((1, 2, 3, 2, 1, 4, 5, 1, 2)))
print(finder((5, 4, 3, 2, 1)))
print(finder((1, 3, 5, 7, 9)))