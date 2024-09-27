from geron import geron

if __name__ == '__main__':
    a = int(input("Введите длину первой стороны: "))
    b = int(input("Введите длину второй стороны: "))
    c = int(input("Введите длину третьей стороны: "))
    print(f"Площадь треугольника равна {geron(a, b, c)}")