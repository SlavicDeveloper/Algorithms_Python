"""Пузырьковая сортировка в обратную сторону"""

import random
import timeit

# Вариант с флагом

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

#orig_list = [random.randint(-100, 100) for _ in range(10)]
#print(bubble_sort_rev(orig_list))


orig_list = [random.randint(-100, 100) for _ in range(10)]
print(
    timeit.timeit(
        "bubble_sort_rev(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]
print(
    timeit.timeit(
        "bubble_sort_rev(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(500)]
print(
    timeit.timeit(
        "bubble_sort_rev(orig_list[:])",
        globals=globals(),
        number=1000))


# Стандартная реализация

def bubble_sort_rev_2(lst_obj):
    """Пузырьковая сортировка в обратную сторону"""
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]

        n += 1
    return lst_obj

#orig_list_1 = [random.randint(-100, 100) for _ in range(10)]
#print(bubble_sort_rev_2(orig_list_1))

orig_list_1 = [random.randint(-100, 100) for _ in range(10)]
print(
    timeit.timeit(
        "bubble_sort_rev(orig_list_1[:])",
        globals=globals(),
        number=1000))

orig_list_1 = [random.randint(-100, 100) for _ in range(100)]
print(
    timeit.timeit(
        "bubble_sort_rev(orig_list_1[:])",
        globals=globals(),
        number=1000))

orig_list_1 = [random.randint(-100, 100) for _ in range(500)]
print(
    timeit.timeit(
        "bubble_sort_rev(orig_list_1[:])",
        globals=globals(),
        number=1000))