"""Merge sort иным способом"""

import random
from memory_profiler import profile


def merge_list(list_a, list_b):
    """Функция соединяет отсортированные списки"""
    c = []
    len_a = len(list_a)
    len_b = len(list_b)

    i = 0
    j = 0
    while i < len_a and j < len_b:
        if list_a[i] <= list_b[j]:
            c.append(list_a[i])
            i += 1
        else:
            c.append(list_b[j])
            j += 1

    c += list_a[i:] + list_b[j:]
    return c




def split_and_merge_list(a):
    """Функция деления списка и слияния списков в общий отсортированный список функцией merge_list"""
    middle = len(a) // 2
    right = a[:middle]
    left = a[middle:]

    if len(right) > 1:
        right = split_and_merge_list(right)
    if len(left) > 1:
        left = split_and_merge_list(left)
    return merge_list(right, left)


rand_list = [random.randint(-100, 100) for _ in range(100)]
print(f"Входной список: {rand_list}")
l = split_and_merge_list(rand_list)
print(f"Выходной список: {l}")