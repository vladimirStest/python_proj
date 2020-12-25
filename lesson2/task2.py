# Задание 2
list_of_values = []
new_list_of_values = []
list_of_keys = []
dict_of_values = {}
while True:
    value = input('Введите добавляемое значение или слово \'Конец\', если список полон: ')
    if value == 'Конец':
        break
    list_of_values.append(value)

for key, value in enumerate(list_of_values):
    if key % 2 == 0:
        dict_of_values[key + 1] = value
    else:
        dict_of_values[key - 1] = value
print(dict_of_values)
list_of_keys.extend(dict_of_values.keys())
list_of_keys.sort()
print(list_of_keys)

for key in list_of_keys:
    new_list_of_values.append(dict_of_values[key])
print(new_list_of_values)