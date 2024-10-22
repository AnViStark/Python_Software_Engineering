with open("Py7//input.txt", "a+") as f:
    f.write("\nThis is new line!")

with open("Py7//input.txt", "r") as f:
    print(f.readlines())
