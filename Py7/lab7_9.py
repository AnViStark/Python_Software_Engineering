def long_word(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_len = len(max(words, key=len))
        for word in words:
            if len(word) == max_len:
                sought_words = word
        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words


print(long_word("Py7//input.txt"))