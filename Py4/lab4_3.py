def main(this, that):
    res = this + that
    return res

if __name__ == '__main__':
    for i in range(3):
        answer = main(i, i + 1)
        print(answer)