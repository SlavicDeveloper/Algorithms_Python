"""Код, позволяющий получить столько нечетных чисел, сколько задал пользователь"""

import memory_profiler


def decor(func):
    """Функция-обертка"""
    def wrapper(*args, **kwargs):
        """Функция для подсчета затраченной памяти"""
        m1 = memory_profiler.memory_usage()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper

# Реализация без уменьшения объема памяти (0.125 MiB)
@decor
def odd_nums_gen(max_num):
    """Функция получает на вход число, которое отражает количество выведенных четных чисел"""
    list_of_nums = []
    max_num = int(max_num)
    for el in range(1, max_num + 1, 2):
        list_of_nums.append(el)
    return list_of_nums


odd_nums = odd_nums_gen(input())
print(*odd_nums)


# Реализация посредством использования "ленивых" вычислений (0.03515625 MiB).
# Такие вычисления позволяют нам использовать генераторы, они же возвращают один
# элемент за другим (то есть мы откладываем вычисления до нужной поры, экономя память)
@decor
def odd_nums_gen_2(max_num):
    """Функция получает на вход число, которое отражает количество выведенных четных чисел"""
    max_num = int(max_num)
    for el in range(1, max_num + 1, 2):
        yield el


if __name__ == '__main__':

    my_generator, mem_diff = odd_nums_gen_2(input())
    list_of_gen = []
    for i in my_generator:
        list_of_gen.append(i)
    print(*list_of_gen)
    print(mem_diff)