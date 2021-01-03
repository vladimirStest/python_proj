# Задание 1:
import re


class Matrix:

    def __init__(self, list_of_lists: list):
        self.list_of_lists = list_of_lists

    def __str__(self):
        # менее предпочтительный вариант
        # # matrix_dict = {key: value for key, value in enumerate(self.list_of_lists)}
        # result = ""
        # for value in self.list_of_lists:
        #     for el in value:
        #         result += f"{el} "
        #     result = re.sub(" $", "\n", result)
        # result = re.sub("\n$", "", result)
        # return result

        # более предпочтительный вариант
        l1 = []
        for el in self.list_of_lists:
            l2 = [str(i) for i in el]
            l1.append(" ".join(l2))
        return "\n".join(l1)

    def __add__(self, other):
        # new_l = [list(map(int, x.split(" "))) for x in str(self).split("\n")]
        list_1 = self.list_of_lists
        list_2 = other.list_of_lists
        new_list = list_1.copy()

        if len(list_1) == len(list_2) & len(list_1[0]) == len(list_2[0]):
            for n1 in range(len(list_1)):
                for n2 in range(len(list_1[0])):
                    new_list[n1][n2] = list_1[n1][n2] + list_2[n1][n2]
            return new_list
        else:
            raise RuntimeError("Для сложения подходят только матрицы с одинаковым числом строк и столбцов")


mc1 = Matrix([[0, 1], [2, 3]])
mc2 = Matrix([[4, 5], [6, 7]])

print(mc1)
print(mc1 + mc2)
print(f"{mc1}\n")
print(mc2)

# тренировка
# p1 = [1, 2]
# p2 = [3, 4]
#
# print(list(map((lambda x, y: x + y), p1, p2)))
# print(sorted(p1, key=lambda x: x % 2, reverse=True))
# print(list(filter(lambda x: x > 1, p1)))
