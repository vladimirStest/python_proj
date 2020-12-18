# Задание 6
def int_func(text):
    list_text = text.split(" ")
    new_text = ""
    for i in list_text:
        new_text = f"{new_text}{i.capitalize()} "
    return new_text


print(int_func("text number 1"))
