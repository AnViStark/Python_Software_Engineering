lines = ["one", "two", "three"]
with open("Py7//input.txt", "w") as f:
    for line in lines:
        f.write(line + "\n")
    print("Done!")