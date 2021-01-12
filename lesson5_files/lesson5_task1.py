# Задание 1
file_name = "file.txt"

if __name__ == '__main__':
    txt = "Введите строку для записи в файл или enter для окончания ввода: "

# Просьба ввести именно строчки ниже, так как данный файл импортируется далее в lesson5_task2.py и lesson5_task3.py
# иванов 10000
# петров 35001
# сидор 15000
def get_record():
    return f"{input(txt)}\n"


def record_is_not_empty(new_record):
    return len(new_record.strip()) > 0


if __name__ == '__main__':
    with open("file.txt", "w", encoding="utf-8") as f_obj:
        new_record = get_record()
        while record_is_not_empty(new_record):
            f_obj.write(new_record)
            new_record = get_record()
