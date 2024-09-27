import random

def cube():
    value = random.randint(1, 6)
    print(f"Выпало число {value}")

    if value == 1 or value == 2:
        print("Вы проиграли")
    elif value == 5 or value == 6:
        print("Вы выиграли")
    else:
        cube()

if __name__ == '__main__':
    cube()