def to_my_set(array):
    my_set = set()
    for i in array:
        my_set.add(i)

        if array.count(i) > 1:
            for k in range(2, array.count(i) + 1):
                my_set.add(str(i) * k)
                
    return my_set

if __name__ == '__main__':
    list_1 = [1, 1, 3, 3, 1]
    list_2 = [5, 5, 5, 5, 5, 5, 5]
    list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
    print(to_my_set(list_1))
    print(to_my_set(list_2))
    print(to_my_set(list_3))