# Задание 1:
from sys import argv


def get_salary():
    error_mes = ("Для корректного расчёта зп необходимо в скрипт 2-м, 3-м и 4-м параметром передавать, " +
                 "соответственно, выработку в часах, ставку в час и премию")
    if len(argv) < 4:
        print(error_mes)
        return
    try:
        [hours, salary_in_hour, bonus] = [int(argv[1]), int(argv[2]), int(argv[3])]
        salary = hours * salary_in_hour + bonus
        print(f"заработная плата сотрудника = {salary}")
        return salary
    except ValueError:
        print(error_mes)


get_salary()
