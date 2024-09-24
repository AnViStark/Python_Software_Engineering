sentence = input("Введите предложение: ")
length = 0
for i in sentence:
    length += 1
print("Длина предложения:", length)
low_sentence = sentence.lower()
print("Предложение в нижнем регистре: ", low_sentence)
vowels = "aeiou"
count = 0
for j in low_sentence:
    if j in vowels:
        count += 1
print("Количество гласных: ", count)
beauty_sentence = ""
i = 0
while i < length:
    if low_sentence[i:i+4] == "ugly":
        beauty_sentence += "beauty"
        i += 4
    else:
        beauty_sentence += low_sentence[i]
        i += 1
print("Предложение после замены: ", beauty_sentence)
if low_sentence[:3] == "the" and low_sentence[-3:] == "end":
    print("Предложение начинается с The и заканчивается на end")
else:
    print("Предложение не начинается с The или не заканчивается на end")