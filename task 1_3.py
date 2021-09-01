"""Код для эмпирической оценки вставки и поиска элементов в словаре и списке"""

import timeit

num_list = []
num_dict = {}


def list_app(el=0, i=1):
    """Функция по заполнению списка"""
    while el <= 4:
        num_list.append(i)  # O(1)
        el += 1
        i += 1
    return num_list


def dict_app(el=0, i=1):
    """Функция по заполнению словаря"""
    while el <= 4:
        num_dict[i] = i  # O(1)
        el += 1
        i += 1
    return num_dict


print(list_app())
print(timeit.timeit(stmt="list_app()", setup="from __main__ import list_app", number=1,
                    globals=globals()))
print(dict_app())
print(timeit.timeit(stmt="dict_app()", setup="from __main__ import dict_app", number=1,
                    globals=globals()))


# При одинаковых константных сложностях операция заполнения словаря происходит быстрее,
# чем заполнение списка

def list_find():
    """Функция поиска элемента в списке"""
    for parts in num_list:  # O(n)
        if parts == 4:  # O(1)
            return parts  # O(1)


def dict_find():
    """Функция поиска элемента в словаре"""
    if num_dict[4] == 4:  # O(1)
        return num_dict[4]  # O(1)


print(list_find())
print(timeit.timeit(stmt="list_find()", setup="from __main__ import list_find", number=1,
                    globals=globals()))
print(dict_find())
print(timeit.timeit(stmt="dict_find()", setup="from __main__ import dict_find", number=1,
                    globals=globals()))

# При выполнении поиска конкретного значения словарь справляется гораздо быстрее,
# так как из хеш-таблиц значения берутся быстрее, чем из списков
