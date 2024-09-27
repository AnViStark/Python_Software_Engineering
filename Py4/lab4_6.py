def first(**kwargs):
    for i, j in kwargs.items():
        print(f"{i} sr.arifmetic {value(j)}")

def value(j):
    return sum(j) / len(j)

if __name__ == '__main__':
    first(x = [1,2,3], y = [4,5,6], z = [7,8,9], w = [10,11,12])