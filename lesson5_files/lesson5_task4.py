# Задание 4
file_name = "file_for_task4.txt"
new_file_name = "new_file_for_task4.txt"


def get_russian_dict(new_record: dict):
    dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    return {dict[key]: value for key, value in new_record.items()}


def get_english_dict():
    with open(file_name, "r", encoding="utf-8") as f_obj:
        old_dict = {}
        for line in f_obj.readlines():
            lines = line.split(" ")
            old_dict[lines[0]] = f"{lines[1]} {lines[2]}"
        return old_dict


new_dict = get_russian_dict(get_english_dict())
with open(new_file_name, "w", encoding="utf-8") as f_obj:
    f_obj.writelines(f"{key} {value}" for key, value in new_dict.items())
