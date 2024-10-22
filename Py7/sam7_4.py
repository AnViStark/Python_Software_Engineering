def stars(input):
    with open('Py7//input.txt','r') as f:
        file = f.read().lower()
        words = list(file.split())
        input = input.lower()
        for word in words:
            input=input.replace(word,"*"*len(word))
        print(input)

stars("Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!")