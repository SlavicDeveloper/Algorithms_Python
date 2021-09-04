"""Работа с timeit и cProfiler"""

from timeit import Timer
from cProfile import run


def revers_1(enter_num, revers_num=0):
    """Функция возврата числа в реверсивной форме"""
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)

t1 = Timer("revers_1(102)", "from __main__ import revers_1")
print(t1.timeit(number=1000))


def revers_2(enter_num, revers_num=0):
    """Функция возврата числа в реверсивной форме"""
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num

t2 = Timer("revers_2(102)", "from __main__ import revers_2")
print(t2.timeit(number=1000))


def revers_3(enter_num):
    """Функция возврата числа в реверсивной форме"""
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

t3 = Timer("revers_3(102)", "from __main__ import revers_3")
print(t3.timeit(number=1000))

run('revers_1(102)')

run('revers_2(102)')

run('revers_3(102)')
