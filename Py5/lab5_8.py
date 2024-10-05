from random import randint

def list_fabric():
    list = [randint(1, 100)] * randint(3, 10)
    return list

if __name__ == '__main__':
    final_list = []
    for i in range(randint(1, 7)):
        final_list.append(list_fabric())
    print(final_list)