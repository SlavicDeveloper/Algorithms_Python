# Задание 2_1. Общая сложность O(n^2)
""" Строка документации к модулю
Данный код ориентирован на поиск минимального значения последовательности
"""


def search_min_num(num_list):
    """Строка документации к функции
    Поиск минимального значения осуществляется при использовании двух циклов "for"
    """
    for i in num_list:  # O(n)
        min_num = i  # O(1)
        for j in range(len(num_list)):  # O(n)
            if min_num > num_list[j]:  # O(1)
                min_num = num_list[j]  # O(1)
    return min_num  # O(1)


num_list = [5, 1, 2, 0]
print(search_min_num(num_list))
