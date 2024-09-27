def main(*args):
    count, sum = 0, 0
    for i in args:
        sum += i
        count += 1
    return sum / count

print(main(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))