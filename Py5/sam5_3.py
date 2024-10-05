from math import sqrt

def geron(a,b,c):
    p=(a+b+c)/2
    s=sqrt(p*(p-a)*(p-b)*(p-c))
    return s

if __name__ == '__main__':
    one = [12, 25, 3, 48, 71]
    two = [5, 18, 40, 62, 98]
    three = [4, 21, 37, 56, 84]

    print(f"Наименьшая площадь: {geron(min(one), min(two), min(three))}")
    print(f"Наибольшая площадь: {geron(max(one), max(two), max(three))}")