def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()

def vowel_words_func(text):
    vowels = 'aeiouAEIOU'
    words = text.split()
    vowel_words = set()
    for word in words:
        cleaned_word = word.strip(",.?!;:")
        if cleaned_word and cleaned_word[0] in vowels:
            vowel_words.add(cleaned_word.lower())
    return vowel_words

def five_letter(text):
    words = text.split()
    count = 0

    for word in words:
        cleaned_word = word.strip(",.?!;:")
        if len(cleaned_word) == 5:
            count += 1
    return count

def replace_digits(text):
    modified_text = ""
    for char in text:
        if char.isdigit():
            modified_text += "#"
        else:
            modified_text += char
    return modified_text

def process_text_file(input_file, output_file):
    text = read_file(input_file)

    vowel_words = vowel_words_func(text)
    print(f"Уникальные слова, начинающиеся с гласных: {', '.join(vowel_words)}")

    five_letter_count = five_letter(text)
    print(f"Количество слов из 5 букв: {five_letter_count}")
    modified_text = replace_digits(text)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(modified_text)

input_file = 'Py7//input.txt'
output_file = 'Py7//output.txt'

process_text_file(input_file, output_file)
