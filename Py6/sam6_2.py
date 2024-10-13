def delete_element(my_tuple, elm):
    tmp = list(my_tuple)
    if elm in tmp:
        tmp.remove(elm)
        my_tuple = tuple(tmp)
        return my_tuple
    else:
        return my_tuple

my_tuple1 = (1, 2, 3)
my_tuple2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
my_tuple3 = (2, 4, 6, 6, 4, 2)

print(delete_element(my_tuple1, 1))
print(delete_element(my_tuple2, 3))
print(delete_element(my_tuple3, 9))