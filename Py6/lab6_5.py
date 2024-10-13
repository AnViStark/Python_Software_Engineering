def tuple_sort(my_tuple):
    for element in my_tuple:
        if not isinstance(element, int):
            return my_tuple
    return tuple(sorted(my_tuple))

if __name__ == '__main__':
    print(tuple_sort((5, 5, 3, 1, 9)))
    print(tuple_sort((5, 5, 2.1, '1', 9)))