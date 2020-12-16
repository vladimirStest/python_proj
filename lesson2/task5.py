# Задание 5
my_list = [7, 5, 3, 3, 2]
my_list_copy = my_list.copy()
index = 'index'

# 1 вариант решения
new_element = int(input("Введите новый элемент рейтинга: "))
while new_element in my_list_copy:
    index = my_list_copy.index(new_element)
    my_list_copy[index] = new_element - 1
if index == 'index':
    my_list.append(new_element)
    my_list.sort(reverse=True)
else:
    my_list.insert(index, new_element)
print(f"Новый рейтинг: {my_list}")

# 2 вариант решения:
new_element = int(input("Введите новый элемент рейтинга: "))
count_of_new_element = my_list.count(new_element)
if count_of_new_element != 0:
    index = my_list.index(new_element) + count_of_new_element
    my_list.insert(index, new_element)
else:
    my_list.append(new_element)
    my_list.sort(reverse=True)
print(f"Новый рейтинг: {my_list}")