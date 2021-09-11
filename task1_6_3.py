"""Код, выводящий на экран тип объекта из списка"""
from memory_profiler import profile

# Версия без оптимизации (версия с оптимизацией лежит в файле task_1_6_3_1)
@profile
def type_el():
    """Итерируем по спискус целью определения типа каждого объекта"""
    el_list = []
    num_list = [15 * 3, 15 / 3, 15 // 2, 15**2]
    for element in num_list:
        el_list.append(type(element))
    return el_list

print(type_el())




