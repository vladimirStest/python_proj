# Задание 3
import lesson5_task1


def get_surname(new_record):
    return new_record.split(" ")[0]


def get_salary(new_record):
    return float(new_record.split(" ")[1].strip())


def print_inf_about_poor_employees(dict):
    print(dict)
    poor_employees = [surname for surname, salary in dict.items() if salary < 20000]
    print(f"Сотрудники компании за чертой бедности: {poor_employees}")


def get_average(dict):
    return round(sum(salary for salary in dict.values()) / len(dict), 2)


with open(lesson5_task1.file_name, "r", encoding="utf-8") as f_obj:
    dict = {}
    for line in f_obj.readlines():
        if lesson5_task1.record_is_not_empty(line):
            dict[get_surname(line)] = get_salary(line)
    print_inf_about_poor_employees(dict)
    print(f"Средняя величина дохода всех сотрудников = {get_average(dict)}")
