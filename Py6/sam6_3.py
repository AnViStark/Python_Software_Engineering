import collections

def dict_maker(string):
    digit_dict = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 0: None}
    for i in digit_dict:
        digit_dict[i] = str(string).count(str(i))

    dict2 = {}
    for _ in range(3):
        key = max(digit_dict, key=lambda k: digit_dict[k])
        dict2[key] = digit_dict[key]
        digit_dict.pop(key)

    sorted_dict2 = dict(sorted(dict2.items()))
    return sorted_dict2

random_int = 56241641562165146349841515610564
print(dict_maker(random_int))
