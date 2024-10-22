# Тема 7. Работа с файлами(ввод, вывод).
Отчет по Теме #7 выполнил:
- Винокуров Андрей Николаевич
- АИС-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + | - |
| Задание 7 | + | - |
| Задание 8 | + | - |
| Задание 9 | + | - |
| Задание 10 | + | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.

### Результат.
![Меню](https://github.com/AnViStark/Python_Software_Engineering/blob/Tema_7/Topic7/lab7_1.png?raw=true)

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

```python
file = open("Py7\\input.txt", "r")
print(file.readline())
file.close()
```

### Результат.
![Меню](https://github.com/AnViStark/Python_Software_Engineering/blob/Tema_7/Topic7/lab7_2.png?raw=true)

## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().

```python
f = open("Py7//input.txt", "r")
print(f.readlines())
f.close()
```

### Результат.
![Меню](https://github.com/AnViStark/Python_Software_Engineering/blob/Tema_7/Topic7/lab7_3.png?raw=true)


## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

```python
with open('Py7//input.txt', 'r') as f:
    print(f.readlines())
```

### Результат.
![Меню](https://github.com/AnViStark/Python_Software_Engineering/blob/Tema_7/Topic7/lab7_4.png?raw=true)

## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

```python
with open("Py7//input.txt", "r") as f:
    for line in f:
        print(line)
```

### Результат.
![Меню](https://github.com/AnViStark/Python_Software_Engineering/blob/Tema_7/Topic7/lab7_5.png?raw=true)


## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в в файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

```python
with open("Py7//input.txt", "a+") as f:
    f.write("\nThis is new line!")

with open("Py7//input.txt", "r") as f:
    print(f.readlines())
```

### Результат.
![Меню](https://github.com/AnViStark/Python_Software_Engineering/blob/Tema_7/Topic7/lab7_6.png?raw=true)


## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.

```python
lines = ["one", "two", "three"]
with open("Py7//input.txt", "w") as f:
    for line in lines:
        f.write(line + "\n")
    print("Done!")
```

### Результат.
![Меню](https://github.com/AnViStark/Python_Software_Engineering/blob/Tema_7/Topic7/lab7_7.png?raw=true)

## Лабораторная работа №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).

```python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f"Папка {catalog[0]} содержит: ")
        print(f'Директории: {", ".join(catalog[1])}')
        print(f'Файлы: {", ".join(catalog[2])}')
        print('-' * 40)

print_docs("C:\\Andreys\\MyBlender")
```

### Результат.
![Меню](https://github.com/AnViStark/Python_Software_Engineering/blob/Tema_7/Topic7/lab7_8.png?raw=true)

## Лабораторная работа №9
### Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).

```python
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
```

### Результат.
![Меню](https://github.com/AnViStark/Python_Software_Engineering/blob/Tema_7/Topic7/lab7_9.png?raw=true)

## Лабораторная работа №10
### Требуется создать csv-файл «rows_300.csv» со следующими столбцами: · № - номер по порядку (от 1 до 300); · Секунда - текущая секунда на вашем ПК; · Микросекунда - текущая миллисекунда на часах. Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.

```python
import csv
import datetime
import time

with open("Py7//rows_300.csv", "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["№", "Секунда", "Микросекунда"])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second, 
                         datetime.datetime.now().microsecond])
        time.sleep(0.01)
```

### Результат.
![Меню](https://github.com/AnViStark/Python_Software_Engineering/blob/Tema_7/Topic7/lab7_10.png?raw=true)

## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

```python
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
```

### Результат.
![Меню](https://github.com/AnViStark/Python_Software_Engineering/blob/Tema_7/Topic7/sam7_1.png?raw=true)
![Меню](https://github.com/AnViStark/Python_Software_Engineering/blob/Tema_7/Topic7/article.png?raw=true)
## Выводы
В данной программе была создана функция count_words_in_file, которая принимает имя файла в качестве аргумента и выполняет следующие действия: читает содержимое статьи из файла, преобразует его в нижний регистр, удаляет знаки препинания и разделяет текст на слова. Затем функция подсчитывает общее количество слов и частоту встречаемости каждого слова с помощью словаря. Наконец, функция в цикле находит самое часто встречающееся слово и выводит его вместе с количеством его вхождений.

## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

```python
def add_position():
    date = input("Введите дату покупки: ")
    category = input("На что было потрачено: ")
    amount = float(input("Сумма траты: "))
    
    with open("Py7//traty.txt", "a") as file:
        file.write(f"{date}, {category}, {amount}\n")

def all_positions():
    try:
        with open("Py7//traty.txt", "r") as file:
            expenses = file.readlines()
            if expenses:
                print("Список трат:")
                for expense in expenses:
                    print(expense.strip())
            else:
                print("Данные о расходах отсутствуют.")
    except FileNotFoundError:
        print("Файл с расходами не найден.")

def main():
    while True:
        print("\nМеню:")
        print("1. Добавить расход")
        print("2. Показать всё")
        print("3. Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            add_position()
        elif choice == "2":
            all_positions()
        elif choice == "3":
            break
        else:
            print("Некорректный ввод")

if __name__ == "__main__":
    main()
```

### Результат.
![Меню](https://github.com/AnViStark/Python_Software_Engineering/blob/Tema_7/Topic7/sam7_2.png?raw=true)
![Меню](https://github.com/AnViStark/Python_Software_Engineering/blob/Tema_7/Topic7/traty.png?raw=true)
## Выводы
В данной программе cоздана функция add_position, которая позволяет пользователю ввести информацию о расходах, такую как дата, предмет траты и сумму. Затем информация сохраняется в файл "traty.txt" через метод write. Функция all_positions выводит все расходы, которые были сохранены в файле, таким образом: в переменную expenses записывается содержимое файла, если файл пустой, то выводится сообщение, что данные отсутствуют. В функции main создается бесконечный цикл, который позволяет пользователю выбирать между добавлением расходов, просмотром всех расходов и выходом из программы.


## Лабораторная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.

```python
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
```

### Результат.
![Меню](https://github.com/AnViStark/Python_Software_Engineering/blob/Tema_7/Topic7/sam7_3.png?raw=true)
## Выводы
В данной программе создана функция statistics, которая принимает имя файла в качестве аргумента. Сначала создается список всех латинских букв, затем открывается файл для чтения и считывается каждая строка. Для каждой строки подсчитывается количество латинских букв, слов и строк. В конце выводится необходимая статистика по тексту. 

## Лабораторная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра.

```python
def stars(input):
    with open('Py7//input.txt','r') as f:
        file = f.read().lower()
        words = list(file.split())
        input = input.lower()
        for word in words:
            input=input.replace(word,"*"*len(word))
        print(input)

stars("Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!")
```

### Результат.
![Меню](https://github.com/AnViStark/Python_Software_Engineering/blob/Tema_7/Topic7/sam7_4.png?raw=true)
## Выводы
В данной программе создана функция stars, которая принимает строку в качестве аргумента. Сначала открывается файл input.txt для чтения и считывается содержимое файла в нижнем регистре. Затем создается список запрещенных слов из файла. Далее введенная строка также приводится к нижнему регистру. Затем происходит замена запрещенных слов на звездочки, где бы они ни встречались, даже в середине другого слова с помощью метода replace.

## Лабораторная работа №5
### Напишите программу, которая принимает на вход текстовый файл, содержащий произвольное количество предложений. Программа должна: найти и вывести в консоль все уникальные слова в тексте, которые начинаются с гласных букв, подсчитать и вывести в консоль количество слов в тексте, содержащих ровно 5 букв, заменить все цифры в тексте на символ # и сохранить изменённый текст в новый файл.

```python
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

```

### Результат.
![Меню](https://github.com/AnViStark/Python_Software_Engineering/blob/Tema_7/Topic7/sam7_4.png?raw=true)
## Выводы
В данной программе создана функция read_file, которая принимает имя файла в качестве аргумента и возвращает содержимое файла в виде строки. Затем создана функция vowel_words_func, которая принимает текст в качестве аргумента и возвращает множество уникальных слов, начинающихся с гласных букв. Сначала создается множество гласных букв, затем текст разбивается на слова, и для каждого слова проверяется, начинается ли оно с гласной буквы. Если да, то слово добавляется в множество уникальных слов. Затем создана функция five_letter, которая принимает текст в качестве аргумента и возвращает количество слов, содержащих ровно 5 букв. Текст разбивается на слова, и для каждого слова проверяется, содержит ли оно ровно 5 букв. Если да, то счетчик увеличивается на 1. Затем создана функция replace_digits, которая принимает текст в качестве аргумента и возвращает текст, в котором все цифры заменены на символ #. Текст проходит посимвольно, и если символ является цифрой, то вместо него ставится символ #. Затем создана функция process_text_file, которая принимает имя входного файла и имя выходного файла в качестве аргументов. Сначала считывается содержимое входного файла с помощью функции read_file. Затем вызываются функции vowel_words_func, five_letter и replace_digits для обработки текста. Затем создается новый файл с именем выходного файла и содержимым, полученным после вызова функции replace_digits.

## Общие выводы по теме
В результате выполнения работы были изучены основы работы с файлами в Python, а именно cоздание, чтение, запись и обработка текстовых файлов. 