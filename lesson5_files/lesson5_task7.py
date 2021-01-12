# Задание 7
import json

file_name = "file_for_task7.txt"
new_file_name = "file_for_task7.json"
dict_of_profit = {}
dict_of_average_profit = {}
dict_of_loss = {}
list_of_dict = [{"Profit": dict_of_profit}, {"Common": dict_of_average_profit}, {"Loss": dict_of_loss}]


def get_profit(TR, TC):
    return int(TR) - int(TC)


with open(file_name, "r", encoding="utf-8") as f_obj:
    for line in f_obj.readlines():
        part = line.split(" ")
        if get_profit(part[2], part[3]) > 0:
            dict_of_profit[part[0]] = get_profit(part[2], part[3])
            dict_of_average_profit["average_profit"] = sum(dict_of_profit.values()) / len(dict_of_profit)
        else:
            dict_of_loss[part[0]] = abs(get_profit(part[2], part[3]))
    print(list_of_dict)

with open(new_file_name, "w") as write_f:
    json.dump(list_of_dict, write_f)
