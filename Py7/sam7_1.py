def count_words_in_file(name):
    with open(name, 'r', encoding='utf-8') as file:
        text = file.read()
    text = text.lower()
    for char in ",.!?;:-()[]{}\"'":
        text = text.replace(char, ' ')  
    words = text.split()
    word_count = {}
    total_words = 0
    for word in words:
        total_words += 1
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    most_common_word = None
    most_common_count = 0
    for word, count in word_count.items():
        if count > most_common_count:
            most_common_word = word
            most_common_count = count

    print(f"Общее количество слов: {total_words}")
    print(f"Самое частое слово: '{most_common_word}' встречается {most_common_count} раз.")

count_words_in_file('Py7//article.txt')
