latin_letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

def statistics(filename):
    num_letters = 0
    num_words = 0
    num_lines = 0
    
    try:
        with open(filename, "r") as file:
            for line in file:
                num_lines += 1
                words = line.split()
                num_words += len(words)
                
                for word in words:
                    for char in word:
                        if char in latin_letters:
                            num_letters += 1
        
        print(f"Input file contains:")
        print(f"{num_letters} letters")
        print(f"{num_words} words")
        print(f"{num_lines} lines")
    
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")

if __name__ == "__main__":
    statistics("Py7//input.txt")
