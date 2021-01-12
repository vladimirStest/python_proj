# Задание 6
file_name = "file_for_task6.txt"


def get_int(word):
    if word[0].isdigit():
        return int("".join(str(i) for i in word if i.isdigit()))
    else:
        return 0


with open(file_name, "r", encoding="utf-8") as f_obj:
    dict = {}
    for line in f_obj.readlines():
        part = line.split(" ")
        dict[part[0]] = get_int(part[1]) + get_int(part[2]) + get_int(part[3])
    print(f"Получившийся словарь предметов = {dict}")
