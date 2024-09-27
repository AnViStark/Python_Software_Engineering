def main(**kwargs):
    for i in kwargs.items():
        print(i[0], i[1])
    print()
    for i in kwargs:
        print(i, kwargs[i])

if __name__ == '__main__':
    main(x = [1, 2, 3], y = [4, 5, 6], z = [7, 8, 9])