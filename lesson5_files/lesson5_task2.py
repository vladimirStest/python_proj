# Задание 2
import os

import lesson5_task1


def count_number_of_characters(new_record):
    return len(new_record.strip())


def count_number_of_words(new_record):
    return len(new_record.split(" "))


with open(lesson5_task1.file_name, "r", encoding="utf-8") as f_obj:
    new_record = f_obj.readline()
    line_number = 0
    while lesson5_task1.record_is_not_empty(new_record):
        line_number += 1
        print(f"Cтрока {line_number} = {new_record.strip()}")
        print(f"Количество символов в строке {line_number} = {count_number_of_characters(new_record)}")
        print(f"Количество слов в строке {line_number} = {count_number_of_words(new_record)}\n")
        new_record = f_obj.readline()
    print(f"В файле {os.path.abspath(lesson5_task1.file_name)}\nколичество строк = {line_number}")
