my_dict = {"first": "so easy"}

def dict_maker(**kwargs):
    my_dict.update(kwargs)

dict_maker(a1 = 2, a2 = 3, a3 = 4, tree = "bereza")
print(my_dict)