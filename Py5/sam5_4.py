def beautify(table):
    table = [str(x) for x in table]
    for i in range(len(table)):
        if table[i] == "3":
            table.remove("3")
            table.insert(i, "4")
    table = [x for x in table if x != "2"]
    table = [int(x) for x in table]
    return table

if __name__ == '__main__':
    one, two, three = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4], [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4], [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
    print(f"Исходный список оценок: {one}\nИсправленный: {beautify(one)}")
    print(f"Исходный список оценок: {two}\nИсправленный: {beautify(two)}")
    print(f"Исходный список оценок: {three}\nИсправленный: {beautify(three)}")