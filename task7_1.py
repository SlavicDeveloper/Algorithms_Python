"""Пузырьковая сортировка в обратную сторону"""

import random


def bubble_sort_rev(lst_obj):
    """Пузырьковая сортировка в обратную сторону"""
    n = 1
    flag = True
    while n < len(lst_obj) and flag == True:
        flag = False
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = True
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
print(bubble_sort_rev(orig_list))
