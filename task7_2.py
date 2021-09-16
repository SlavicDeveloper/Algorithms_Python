"""Merge sort иным способом"""
import timeit
import random


# Классический merge sort
def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


# orig_list = [random.randint(-100, 100) for _ in range(10)]
# print(f"Входной список: {orig_list}")
# k = split_and_merge_list(orig_list)
# print(f"Выходной список: {k}")
orig_list = [random.randint(0, 50) for _ in range(10)]
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(0, 50) for _ in range(100)]
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(0, 50) for _ in range(1000)]
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))


# Новый вариант
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

# rand_list = [random.randint(-100, 100) for _ in range(100)]
# print(f"Входной список: {rand_list}")
# l = split_and_merge_list(rand_list)
# print(f"Выходной список: {l}")

rand_list = [random.randint(0, 50) for _ in range(10)]
print(
    timeit.timeit(
        "split_and_merge_list(rand_list[:])",
        globals=globals(),
        number=1000))

rand_list = [random.randint(0, 50) for _ in range(100)]
print(
    timeit.timeit(
        "split_and_merge_list(rand_list[:])",
        globals=globals(),
        number=1000))

rand_list = [random.randint(0, 50) for _ in range(1000)]
print(
    timeit.timeit(
        "split_and_merge_list(rand_list[:])",
        globals=globals(),
        number=1000))