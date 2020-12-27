# Задание 5
file_name = "file_for_task5.txt"
numbers = "1 2 3 4 5 6 7"
with open(file_name, "w+", encoding="utf-8") as f_obj:
    f_obj.write(numbers)
    f_obj.seek(0)
    numbers = [int(number) for number in f_obj.readline().split(" ")]
    print(f"Сумма чисел в файле = {sum(numbers)}")
