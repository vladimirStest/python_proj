# Задание 1
int_var = 100
str_var = "100"

user_int = input("Введите число ")
user_string = input("Введите строку ")
print(f"Пользователь ввёл число {user_int} и строку \"{user_string}\"")

# Задание 2
time = int(input("Введите время в секундах "))

hour = str(time // 3600)
if int(hour) > 24:
    hour = f'{int(hour) % 24}'
if len(hour) == 1:
    hour = f'0{hour}'
time = time - time // 3600 * 3600

minute = str(time // 60)
if len(minute) == 1:
    minute = f'0{minute}'

seconds = str(time - int(minute) * 60)
if len(seconds) == 1:
    seconds = f'0{seconds}'

print(f"Пользователь ввёл время {hour} : {minute} : {seconds}")

# Задание 3
n = input("Введите число n ")
length_n = len(n)
count = 0
digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
while count < length_n:
    if n[count] in digits:
        count += 1
    else:
        if (count == 0) & (n[count] == "-"):
            n = input("Введите, пожалуйста, положительное число n ")
        else:
            n = input("Введите число n, не должно содержаться нецифровых символов ")
        length_n = len(n)
        count = 0

nn = int(n + n)
nnn = int(n + n + n)

sum_of_n = int(n) + nn + nnn
print(f"n + nn + nnn = {sum_of_n}")

# Задание 4
number = input("Введите целое положительное число ")
order = 1
max_value = int(number[0])
while (max_value != 9) & (order < len(number)):
    next_digit = int(number[order])
    if max_value < next_digit:
        max_value = next_digit
    order += 1
print(f'В числе {number} самая большая цифра = {max_value}')

# Задание 5
TR = int(input("Введите выручку фирмы "))
TC = int(input("Введите издержки фирмы "))
total = TR - TC
if total > 0:
    print(f'Фирма получает прибыль {total}')
    print(f'Рентабельность выручки = {round(total / TR, 4)}')
    number_of_employees = int(input("Введите численность сотрудников фирмы "))
    print(f'прибыль фирмы в расчете на одного сотрудника = {round(total / number_of_employees, 4)}')
elif total == 0:
    print(f'Фирма работает безубыточно')
else:
    print(f'Фирма работает с убытком {TC - TR}')

# Задание 6
present_result = int(input("Введите, сколько км вы пробежали сегодня "))
future_result = int(input("Введите, сколько км вы планируете пробегать "))
count = 1

if future_result <= present_result:
    print(f'Вы уже пробегаете необходимое расстояние {future_result} км за день')
else:
    while present_result < future_result:
        present_result *= 1.1
        count += 1
    print(f'на {count}-й день спортсмен достиг результата — не менее {future_result} км')