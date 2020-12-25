# Задание 4
sentence = input('Введите предложение: ')
for word in sentence.split():
    if len(word) > 10:
        print(word[:10])
        continue
    print(word)
