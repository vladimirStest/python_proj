# Задание 3
seasons = {(12, 1, 2): "зима",
           (3, 4, 5): "весна",
           (6, 7, 8): "лето",
           (9, 10, 11): "весна"}

month = int(input('Введите порядковый номер месяца: '))
while not ((month >= 1) & (month <= 12)):
    month = int(input('Введите порядковый номер месяца (число от 1 до 12): '))
for key in seasons.keys():
    if month in key:
        print(f'Месяц под номером {month} принадлежит к времени года \"{seasons[key]}\"')
