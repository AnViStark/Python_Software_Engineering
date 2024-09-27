def main(*args):
    
    if len(args) == 0:
        print("Нет аргументов")
        return
    
    sum, count = 0, 0
    for i in args:
        sum += i
        count += 1
    print(sum / count)

if __name__ == '__main__':
    main(12, 6, 56, 11)