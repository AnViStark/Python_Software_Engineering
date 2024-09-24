value = "string"
for i in range(len(value), 0, -1):
    value = value[:i]
    print(i, value)